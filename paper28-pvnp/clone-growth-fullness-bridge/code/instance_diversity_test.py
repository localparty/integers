"""
Instance Diversity Test -- Node 1.3.5.10

Repair of Lemma 2.6.4 (instance diversity gap) identified by the Path B
Critic (critique 1.3.5.8).

THE GAP: Lemma 2.6.4 claims that for any sequence of distinct polymorphism
pairs at growing arities k, there exists a FIXED witness instance Gamma_0
where the pairs remain delta_0-separated in PU(d_0).  The Critic's objection:
the separation at any fixed instance may vanish as k grows because the
(k-1)-tuple averaging concentrates.

THIS SCRIPT computes, for FIXED 2-SAT instances:
  1. The threshold-k (generalized majority) polymorphism f_k at arities
     k = 3, 5, 7, 9, 11, 13, 15.
  2. The coherent-sum clone operator V_{f_k} (the Path B version, NOT the
     omega-averaged T_f from the killed K-14).
  3. The unitary part U_{f_k} via polar decomposition.
  4. PU-distances d_PU(U_{f_k}, U_{f_{k+2}}) between consecutive arities.
  5. PU-distances d_PU(U_{f_k}, cI) -- distance to nearest scalar.
  6. Repeats for multiple instances at n = 4, 6, 8.

WHAT THE CRITIC NEEDS TO SEE:
  - If d_PU stays bounded below: gap closed.
  - If d_PU -> 0: the lemma needs repair or a different witness.
  - If d_PU(U_{f_k}, scalar) stays bounded below: non-scalarity holds.

Author: Claude Opus 4.6 (1M context), Node 1.3.5.10
Date: 2026-04-11
"""

import numpy as np
from itertools import product as cartesian_product
from scipy.linalg import polar
import sys
import json

np.set_printoptions(precision=8, suppress=True, linewidth=140)
np.random.seed(42)

# ============================================================
# 1. Instance generation (2-SAT)
# ============================================================

def enumerate_solutions_2sat(n, clauses):
    """Brute-force enumerate all solutions of a 2-SAT instance."""
    solutions = []
    for bits in range(2**n):
        assignment = tuple((bits >> i) & 1 for i in range(n))
        if all(evaluate_clause_2sat(assignment, c) for c in clauses):
            solutions.append(assignment)
    return solutions


def evaluate_clause_2sat(assignment, clause):
    """Evaluate a single 2-SAT clause: (var0, sign0, var1, sign1)."""
    v0, s0, v1, s1 = clause
    lit0 = assignment[v0] if s0 == 1 else 1 - assignment[v0]
    lit1 = assignment[v1] if s1 == 1 else 1 - assignment[v1]
    return lit0 or lit1


def make_all_2clauses(n):
    """Generate ALL possible 2-clauses on n variables (the 'all clauses' instance)."""
    clauses = []
    for v0 in range(n):
        for v1 in range(v0 + 1, n):
            for s0 in [0, 1]:
                for s1 in [0, 1]:
                    clauses.append((v0, s0, v1, s1))
    return clauses


def make_sparse_2sat(n, seed=0):
    """Generate a sparse 2-SAT instance with many solutions."""
    rng = np.random.RandomState(seed)
    num_clauses = n  # sparse: ratio 1
    clauses = []
    for _ in range(num_clauses):
        v0, v1 = rng.choice(n, size=2, replace=False)
        s0, s1 = rng.randint(0, 2, size=2)
        clauses.append((int(v0), int(s0), int(v1), int(s1)))
    return clauses


def make_medium_2sat(n, seed=0):
    """Generate a medium-density 2-SAT instance."""
    rng = np.random.RandomState(seed)
    num_clauses = 2 * n
    clauses = []
    for _ in range(num_clauses):
        v0, v1 = rng.choice(n, size=2, replace=False)
        s0, s1 = rng.randint(0, 2, size=2)
        clauses.append((int(v0), int(s0), int(v1), int(s1)))
    return clauses


def make_trivial_instance(n):
    """The trivial instance: no clauses, all 2^n assignments are solutions."""
    return []


# ============================================================
# 2. Generalized majority (threshold-k polymorphism)
# ============================================================

def threshold_majority(args):
    """
    Generalized majority / threshold function on k binary inputs.
    Returns 1 if the sum of inputs >= ceil(k/2), else 0.
    Applied coordinate-wise to n-bit strings.

    args: list of k tuples, each of length n.
    Returns: tuple of length n.
    """
    k = len(args)
    n = len(args[0])
    threshold = (k + 1) // 2  # ceil(k/2)
    result = []
    for j in range(n):
        s = sum(a[j] for a in args)
        result.append(1 if s >= threshold else 0)
    return tuple(result)


def minority_threshold(args):
    """
    Minority function: returns 1 iff sum of inputs < ceil(k/2).
    This is a DIFFERENT polymorphism from majority.
    For 2-SAT: minority is also a polymorphism (the dual).
    """
    k = len(args)
    n = len(args[0])
    threshold = (k + 1) // 2
    result = []
    for j in range(n):
        s = sum(a[j] for a in args)
        result.append(1 if s < threshold else 0)
    return tuple(result)


def verify_polymorphism(solutions, poly_func, k):
    """
    Verify that poly_func is a k-ary polymorphism of the solution set:
    for all (a_1,...,a_k) in Sol^k, poly_func(a_1,...,a_k) must be in Sol.
    """
    sol_set = set(solutions)
    violations = 0
    total = 0
    # For large k and large |Sol|, full enumeration is expensive.
    # Use sampling if the space is too large.
    S = len(solutions)
    if S**k > 500000:
        # Sample
        rng = np.random.RandomState(123)
        for _ in range(min(500000, S**k)):
            indices = rng.randint(0, S, size=k)
            args = [solutions[i] for i in indices]
            result = poly_func(args)
            total += 1
            if result not in sol_set:
                violations += 1
    else:
        for combo in cartesian_product(range(S), repeat=k):
            args = [solutions[i] for i in combo]
            result = poly_func(args)
            total += 1
            if result not in sol_set:
                violations += 1
    return violations == 0, violations, total


# ============================================================
# 3. Coherent-sum clone operator V_f (Path B construction)
# ============================================================

def compute_Vf_coherent(solutions, poly_func, k):
    """
    Compute the coherent-sum clone operator V_f for a k-ary polymorphism.

    V_f[s, a] = (1 / |Sol|^{(k-1)/2}) *
                #{(a^(2),...,a^(k)) in Sol^{k-1} : f(a, a^(2),...,a^(k)) = s}

    This is the PATH B construction: a coherent sum preserving phases,
    NOT the omega-averaged T_f from the killed K-14.

    The key difference from T_f:
      - T_f divides by |Sol|^{k-1} (expectation value / trace).
      - V_f divides by |Sol|^{(k-1)/2} (L2 normalization).
    The V_f construction preserves the operator's phase structure
    and yields a non-trivial polar unitary.

    Returns the |Sol| x |Sol| complex matrix V_f.
    """
    sol_list = list(solutions)
    S = len(sol_list)
    sol_to_idx = {s: i for i, s in enumerate(sol_list)}

    V = np.zeros((S, S), dtype=np.complex128)

    # For each first argument a, sum over all (k-1)-tuples of remaining args
    if S**(k - 1) > 2000000:
        # For very large spaces, sample with importance
        rng = np.random.RandomState(42)
        n_samples = 2000000
        for a_idx, a in enumerate(sol_list):
            counts = np.zeros(S, dtype=np.float64)
            for _ in range(n_samples):
                # Random (k-1)-tuple from Sol^{k-1}
                indices = rng.randint(0, S, size=k - 1)
                args = [a] + [sol_list[i] for i in indices]
                result = poly_func(args)
                if result in sol_to_idx:
                    s_idx = sol_to_idx[result]
                    counts[s_idx] += 1.0
            # Scale: each count represents (S^{k-1} / n_samples) * count hits
            V[:, a_idx] = counts * (S**(k - 1) / n_samples)
    else:
        for a_idx, a in enumerate(sol_list):
            for combo in cartesian_product(range(S), repeat=k - 1):
                args = [a] + [sol_list[i] for i in combo]
                result = poly_func(args)
                if result in sol_to_idx:
                    s_idx = sol_to_idx[result]
                    V[s_idx, a_idx] += 1.0

    # Normalize by |Sol|^{(k-1)/2}
    norm_factor = S**((k - 1) / 2.0)
    V /= norm_factor

    return V


# ============================================================
# 4. Polar decomposition and unitary extraction
# ============================================================

def extract_unitary(V):
    """
    Extract the unitary part U from V via polar decomposition: V = U P.
    Uses scipy.linalg.polar.

    Returns U (unitary matrix).
    """
    U, P = polar(V)
    return U


# ============================================================
# 5. PU-distance computation
# ============================================================

def d_PU(U1, U2):
    """
    Compute the projective unitary distance:
      d_PU([U1], [U2]) = min_{theta in [0, 2pi)} ||U1 - e^{i*theta} * U2||_op

    where ||.||_op is the operator norm (largest singular value of the difference).

    The minimization over theta is done by scanning + refinement.
    """
    best_dist = np.inf
    best_theta = 0.0

    # Coarse scan
    for theta in np.linspace(0, 2 * np.pi, 360, endpoint=False):
        phase = np.exp(1j * theta)
        diff = U1 - phase * U2
        dist = np.linalg.norm(diff, ord=2)  # operator norm
        if dist < best_dist:
            best_dist = dist
            best_theta = theta

    # Refinement around the best theta
    for theta in np.linspace(best_theta - 0.02, best_theta + 0.02, 1000):
        phase = np.exp(1j * theta)
        diff = U1 - phase * U2
        dist = np.linalg.norm(diff, ord=2)
        if dist < best_dist:
            best_dist = dist
            best_theta = theta

    return best_dist, best_theta


def d_PU_to_scalar(U):
    """
    Compute the PU-distance from U to the nearest scalar matrix cI:
      d_PU([U], [cI]) = min_{c in U(1)} ||U - c * I||_op
                       = min_{theta} ||U - e^{i*theta} * I||_op

    This measures how close U is to being a scalar (phase * identity).
    """
    d = U.shape[0]
    I = np.eye(d, dtype=np.complex128)
    return d_PU(U, I)


def d_PU_HS(U1, U2):
    """
    PU-distance using Hilbert-Schmidt norm (Frobenius) instead of operator norm.
    This is sometimes more stable numerically.
      d_PU_HS([U1], [U2]) = min_{theta} ||U1 - e^{i*theta} * U2||_F / sqrt(d)
    """
    d = U1.shape[0]
    best_dist = np.inf
    best_theta = 0.0

    for theta in np.linspace(0, 2 * np.pi, 360, endpoint=False):
        phase = np.exp(1j * theta)
        diff = U1 - phase * U2
        dist = np.linalg.norm(diff, 'fro') / np.sqrt(d)
        if dist < best_dist:
            best_dist = dist
            best_theta = theta

    # Refinement
    for theta in np.linspace(best_theta - 0.02, best_theta + 0.02, 1000):
        phase = np.exp(1j * theta)
        diff = U1 - phase * U2
        dist = np.linalg.norm(diff, 'fro') / np.sqrt(d)
        if dist < best_dist:
            best_dist = dist
            best_theta = theta

    return best_dist, best_theta


def d_PU_to_scalar_HS(U):
    """PU-distance to nearest scalar using HS norm."""
    d = U.shape[0]
    I = np.eye(d, dtype=np.complex128)
    return d_PU_HS(U, I)


# ============================================================
# 6. Structural diagnostics
# ============================================================

def analyze_unitary(U, label=""):
    """Detailed analysis of a unitary matrix."""
    d = U.shape[0]

    # Check unitarity
    err = np.linalg.norm(U @ U.conj().T - np.eye(d))
    is_unitary = err < 1e-10

    # Eigenvalues (should be on unit circle)
    eigvals = np.linalg.eigvals(U)
    phases = np.angle(eigvals)
    moduli = np.abs(eigvals)

    # Trace (divided by d, should be in unit disk)
    tr = np.trace(U) / d

    # Distance to scalar
    dist_scalar_op, _ = d_PU_to_scalar(U)
    dist_scalar_HS, _ = d_PU_to_scalar_HS(U)

    info = {
        "label": label,
        "dim": d,
        "is_unitary": bool(is_unitary),
        "unitarity_error": float(err),
        "eigenvalue_phases": sorted(phases.tolist()),
        "eigenvalue_moduli": sorted(moduli.tolist()),
        "normalized_trace": complex(tr),
        "trace_modulus": float(abs(tr)),
        "dist_to_scalar_op": float(dist_scalar_op),
        "dist_to_scalar_HS": float(dist_scalar_HS),
    }
    return info


# ============================================================
# 7. Main computation
# ============================================================

def run_instance_test(n, clauses, instance_label, arities=None):
    """
    Run the full instance diversity test for a single 2-SAT instance.

    For each arity k in arities:
      - Build the threshold-k majority polymorphism
      - Compute V_{f_k} (coherent-sum clone operator)
      - Extract U_{f_k} via polar decomposition
      - Compute PU-distances between consecutive arities
      - Compute PU-distance to nearest scalar

    Returns a results dictionary.
    """
    if arities is None:
        arities = [3, 5, 7, 9, 11, 13, 15]

    # Enumerate solutions
    solutions = enumerate_solutions_2sat(n, clauses)
    S = len(solutions)
    print(f"\n{'='*80}")
    print(f"Instance: {instance_label}")
    print(f"  n = {n} variables, {len(clauses)} clauses, |Sol| = {S}")
    print(f"  Solution space dimension d = {S}")
    print(f"{'='*80}")

    if S < 2:
        print(f"  SKIP: Need at least 2 solutions, got {S}")
        return None

    # Verify majority is a polymorphism at arity 3 (sanity check)
    is_poly, viols, total = verify_polymorphism(
        solutions, threshold_majority, 3
    )
    print(f"  Majority is arity-3 polymorphism: {is_poly} "
          f"({viols}/{total} violations)")
    if not is_poly:
        print(f"  WARNING: Majority is NOT a polymorphism at this instance!")
        print(f"  This is expected only for non-2-SAT instances.")

    # Collect unitaries
    unitaries = {}
    unitary_info = {}

    for k in arities:
        print(f"\n  --- Arity k = {k} ---")

        # Check feasibility: |Sol|^{k-1} iterations
        iters = S**(k - 1)
        print(f"  V_f construction: {S}^{k-1} = {iters} terms", end="")
        if iters > 2000000:
            print(f" (SAMPLING: 2M samples)")
        else:
            print(f" (exact)")

        # Compute V_f (coherent sum)
        V = compute_Vf_coherent(solutions, threshold_majority, k)

        # Basic V diagnostics
        sv = np.linalg.svd(V, compute_uv=False)
        print(f"  V singular values: min={sv.min():.6f}, max={sv.max():.6f}, "
              f"condition={sv.max()/max(sv.min(), 1e-15):.4f}")
        print(f"  V Frobenius norm: {np.linalg.norm(V, 'fro'):.6f}")

        # Polar decomposition
        U = extract_unitary(V)

        # Verify unitarity
        err = np.linalg.norm(U @ U.conj().T - np.eye(S))
        print(f"  U unitarity error: {err:.2e}")

        # Store
        unitaries[k] = U
        info = analyze_unitary(U, label=f"U_maj(k={k})")
        unitary_info[k] = info

        print(f"  U eigenvalue phases: "
              f"{[f'{p:.4f}' for p in info['eigenvalue_phases']]}")
        print(f"  U normalized trace: {info['normalized_trace']:.6f} "
              f"(|tr/d| = {info['trace_modulus']:.6f})")
        print(f"  d_PU(U, scalar) [op-norm]:  {info['dist_to_scalar_op']:.8f}")
        print(f"  d_PU(U, scalar) [HS-norm]:  {info['dist_to_scalar_HS']:.8f}")

    # -------------------------------------------------------
    # Compute PU-distances between consecutive arities
    # -------------------------------------------------------
    print(f"\n  === PU-distances between consecutive arities ===")
    consecutive_dists_op = []
    consecutive_dists_HS = []

    for i in range(len(arities) - 1):
        k1, k2 = arities[i], arities[i + 1]
        if k1 in unitaries and k2 in unitaries:
            dist_op, theta_op = d_PU(unitaries[k1], unitaries[k2])
            dist_HS, theta_HS = d_PU_HS(unitaries[k1], unitaries[k2])
            consecutive_dists_op.append(dist_op)
            consecutive_dists_HS.append(dist_HS)
            print(f"  d_PU(U_{{k={k1}}}, U_{{k={k2}}}) "
                  f"[op] = {dist_op:.8f}  [HS] = {dist_HS:.8f}  "
                  f"[best phase = {theta_op:.4f}]")

    # -------------------------------------------------------
    # Collect distances to scalar
    # -------------------------------------------------------
    print(f"\n  === PU-distance to nearest scalar (non-scalarity test) ===")
    scalar_dists_op = []
    scalar_dists_HS = []

    for k in arities:
        if k in unitary_info:
            d_op = unitary_info[k]['dist_to_scalar_op']
            d_HS = unitary_info[k]['dist_to_scalar_HS']
            scalar_dists_op.append(d_op)
            scalar_dists_HS.append(d_HS)
            print(f"  d_PU(U_{{k={k}}}, cI) "
                  f"[op] = {d_op:.8f}  [HS] = {d_HS:.8f}")

    # -------------------------------------------------------
    # Trend analysis
    # -------------------------------------------------------
    print(f"\n  === TREND ANALYSIS ===")

    if len(consecutive_dists_op) >= 2:
        # Check if consecutive distances are monotonically decreasing
        diffs = [consecutive_dists_op[i+1] - consecutive_dists_op[i]
                 for i in range(len(consecutive_dists_op) - 1)]
        monotone_decreasing = all(d <= 0 for d in diffs)
        print(f"  Consecutive d_PU monotone decreasing: {monotone_decreasing}")
        print(f"  Consecutive d_PU values: "
              f"{[f'{d:.6f}' for d in consecutive_dists_op]}")
        if consecutive_dists_op[-1] < 1e-6:
            print(f"  VERDICT: d_PU(consecutive) VANISHES --> "
                  f"separation collapses at this instance")
        elif min(consecutive_dists_op) > 0.001:
            print(f"  VERDICT: d_PU(consecutive) BOUNDED BELOW by "
                  f"{min(consecutive_dists_op):.6f} --> separation holds")
        else:
            print(f"  VERDICT: INCONCLUSIVE -- values are small but not yet zero")

    if len(scalar_dists_op) >= 2:
        # Check if scalar distance is monotonically decreasing
        diffs = [scalar_dists_op[i+1] - scalar_dists_op[i]
                 for i in range(len(scalar_dists_op) - 1)]
        monotone_decreasing = all(d <= 0 for d in diffs)
        print(f"\n  Scalar d_PU monotone decreasing: {monotone_decreasing}")
        print(f"  Scalar d_PU values: "
              f"{[f'{d:.6f}' for d in scalar_dists_op]}")
        if scalar_dists_op[-1] < 1e-6:
            print(f"  VERDICT: d_PU(U, scalar) VANISHES --> "
                  f"non-scalarity FAILS at this instance")
        elif min(scalar_dists_op) > 0.01:
            print(f"  VERDICT: d_PU(U, scalar) BOUNDED BELOW by "
                  f"{min(scalar_dists_op):.6f} --> non-scalarity HOLDS")
        else:
            print(f"  VERDICT: INCONCLUSIVE -- values are small but not yet zero")

    # Build results dict
    results = {
        "instance_label": instance_label,
        "n": n,
        "num_clauses": len(clauses),
        "num_solutions": S,
        "arities": arities,
        "majority_is_polymorphism_k3": is_poly,
        "unitary_info": {
            str(k): {
                "dist_to_scalar_op": info["dist_to_scalar_op"],
                "dist_to_scalar_HS": info["dist_to_scalar_HS"],
                "trace_modulus": info["trace_modulus"],
                "eigenvalue_phases": info["eigenvalue_phases"],
            }
            for k, info in unitary_info.items()
        },
        "consecutive_PU_dist_op": consecutive_dists_op,
        "consecutive_PU_dist_HS": consecutive_dists_HS,
        "scalar_PU_dist_op": scalar_dists_op,
        "scalar_PU_dist_HS": scalar_dists_HS,
    }

    return results


# ============================================================
# 8. Cross-polymorphism test: majority vs minority
# ============================================================

def run_cross_polymorphism_test(n, clauses, instance_label, arities=None):
    """
    Compare DIFFERENT polymorphisms (majority vs minority) at the same arity.
    This tests whether two distinct polymorphisms remain PU-separated as k grows.
    """
    if arities is None:
        arities = [3, 5, 7, 9, 11]

    solutions = enumerate_solutions_2sat(n, clauses)
    S = len(solutions)
    print(f"\n{'='*80}")
    print(f"CROSS-POLYMORPHISM TEST: {instance_label}")
    print(f"  n = {n}, |Sol| = {S}")
    print(f"{'='*80}")

    if S < 2:
        print(f"  SKIP: need |Sol| >= 2")
        return None

    # Verify minority is a polymorphism for 2-SAT
    # For 2-SAT with all-positive clauses, minority may not be a polymorphism.
    # We check and report.
    is_min_poly, _, _ = verify_polymorphism(solutions, minority_threshold, 3)
    print(f"  Minority is arity-3 polymorphism: {is_min_poly}")

    if not is_min_poly:
        print(f"  Minority is NOT a polymorphism -- "
              f"skipping cross-polymorphism test.")
        print(f"  (This is expected: minority is NOT a 2-SAT polymorphism")
        print(f"   for general 2-SAT instances. Using projection pi_2 instead.)")
        # Use projection pi_2 as the second polymorphism
        def pi2_func(args):
            """Second projection: returns args[1]."""
            return args[1]
        poly2_func = pi2_func
        poly2_name = "pi_2 (projection)"
    else:
        poly2_func = minority_threshold
        poly2_name = "minority"

    cross_dists_op = []
    cross_dists_HS = []

    for k in arities:
        iters = S**(k - 1)
        if iters > 5000000 and S > 32:
            print(f"  Arity k={k}: SKIP (too large: {S}^{k-1} = {iters})")
            continue

        print(f"\n  --- Arity k = {k} ---")

        V_maj = compute_Vf_coherent(solutions, threshold_majority, k)
        U_maj = extract_unitary(V_maj)

        V_p2 = compute_Vf_coherent(solutions, poly2_func, k)
        U_p2 = extract_unitary(V_p2)

        dist_op, theta = d_PU(U_maj, U_p2)
        dist_HS, _ = d_PU_HS(U_maj, U_p2)
        cross_dists_op.append(dist_op)
        cross_dists_HS.append(dist_HS)
        print(f"  d_PU(U_maj, U_{{{poly2_name}}}) "
              f"[op] = {dist_op:.8f}  [HS] = {dist_HS:.8f}")

    print(f"\n  Cross-polymorphism d_PU trajectory: "
          f"{[f'{d:.6f}' for d in cross_dists_op]}")
    if len(cross_dists_op) >= 2:
        if min(cross_dists_op) > 0.01:
            print(f"  VERDICT: BOUNDED BELOW by {min(cross_dists_op):.6f} --> "
                  f"instance diversity for distinct polymorphisms HOLDS")
        elif cross_dists_op[-1] < 1e-6:
            print(f"  VERDICT: VANISHES --> instance diversity FAILS")
        else:
            print(f"  VERDICT: INCONCLUSIVE")

    return {
        "instance_label": instance_label,
        "poly2_name": poly2_name,
        "arities_tested": arities[:len(cross_dists_op)],
        "cross_PU_dist_op": cross_dists_op,
        "cross_PU_dist_HS": cross_dists_HS,
    }


# ============================================================
# 9. Eigenvalue spread diagnostic
# ============================================================

def eigenvalue_spread_test(n, clauses, instance_label, arities=None):
    """
    Compute the eigenvalue spread of U_{f_k} as k grows.
    The eigenvalue spread measures how 'non-scalar' the unitary is.

    A scalar cI has all eigenvalues equal to c.
    A non-scalar unitary has eigenvalues spread around the unit circle.

    The spread is: max|phase_i - phase_j| over eigenvalue pairs.
    """
    if arities is None:
        arities = [3, 5, 7, 9, 11, 13, 15]

    solutions = enumerate_solutions_2sat(n, clauses)
    S = len(solutions)

    if S < 2:
        return None

    print(f"\n  === Eigenvalue spread diagnostic: {instance_label} ===")

    spreads = []
    for k in arities:
        iters = S**(k - 1)
        if iters > 5000000 and S > 64:
            print(f"  k={k}: SKIP (too large)")
            continue
        V = compute_Vf_coherent(solutions, threshold_majority, k)
        U = extract_unitary(V)
        eigvals = np.linalg.eigvals(U)
        phases = np.sort(np.angle(eigvals))
        if len(phases) >= 2:
            # Max phase gap
            max_spread = max(phases[-1] - phases[0],
                             2*np.pi - (phases[-1] - phases[0]))
            min_spread = min(abs(phases[i+1] - phases[i])
                             for i in range(len(phases)-1))
            spread = phases[-1] - phases[0]
        else:
            spread = 0.0
            min_spread = 0.0
        spreads.append(spread)
        print(f"  k={k}: eigenvalue phases = "
              f"{[f'{p:.4f}' for p in phases]}, "
              f"spread = {spread:.6f}, min_gap = {min_spread:.6f}")

    print(f"  Spread trajectory: {[f'{s:.6f}' for s in spreads]}")
    if len(spreads) >= 2:
        if spreads[-1] < 1e-6:
            print(f"  --> Eigenvalues COLLAPSE to single phase "
                  f"(approaching scalar)")
        elif min(spreads) > 0.01:
            print(f"  --> Eigenvalue spread BOUNDED BELOW by "
                  f"{min(spreads):.6f} (non-scalar)")

    return spreads


# ============================================================
# 10. Main
# ============================================================

def main():
    print("=" * 80)
    print("INSTANCE DIVERSITY TEST -- Node 1.3.5.10")
    print("Repair of Lemma 2.6.4 (Critic gap: PU separation vs arity)")
    print("=" * 80)

    all_results = {}

    # ---------------------------------------------------------
    # Battery of instances at n = 4
    # ---------------------------------------------------------
    n = 4
    print(f"\n{'#'*80}")
    print(f"# BLOCK 1: n = {n}")
    print(f"{'#'*80}")

    # Instance A: trivial (no clauses, |Sol| = 16)
    clauses_A = make_trivial_instance(n)
    res_A = run_instance_test(n, clauses_A, f"n={n} trivial (|Sol|=16)")
    if res_A:
        all_results["n4_trivial"] = res_A
        eigenvalue_spread_test(n, clauses_A, f"n={n} trivial")

    # Instance B: sparse 2-SAT
    clauses_B = make_sparse_2sat(n, seed=0)
    res_B = run_instance_test(n, clauses_B, f"n={n} sparse 2-SAT")
    if res_B:
        all_results["n4_sparse"] = res_B
        eigenvalue_spread_test(n, clauses_B, f"n={n} sparse")

    # Instance C: medium 2-SAT
    clauses_C = make_medium_2sat(n, seed=1)
    res_C = run_instance_test(n, clauses_C, f"n={n} medium 2-SAT")
    if res_C:
        all_results["n4_medium"] = res_C

    # Instance D: all 2-clauses (maximally constrained)
    clauses_D = make_all_2clauses(n)
    res_D = run_instance_test(n, clauses_D, f"n={n} all-clauses")
    if res_D:
        all_results["n4_allclauses"] = res_D

    # ---------------------------------------------------------
    # n = 6 (with adapted arities due to larger Sol sets)
    # ---------------------------------------------------------
    n = 6
    print(f"\n{'#'*80}")
    print(f"# BLOCK 2: n = {n}")
    print(f"{'#'*80}")

    # Sparse instance
    clauses_6s = make_sparse_2sat(n, seed=10)
    # Limit arities to avoid combinatorial explosion
    arities_6 = [3, 5, 7, 9, 11]
    res_6s = run_instance_test(n, clauses_6s, f"n={n} sparse 2-SAT",
                                arities=arities_6)
    if res_6s:
        all_results["n6_sparse"] = res_6s

    # Medium instance
    clauses_6m = make_medium_2sat(n, seed=11)
    res_6m = run_instance_test(n, clauses_6m, f"n={n} medium 2-SAT",
                                arities=arities_6)
    if res_6m:
        all_results["n6_medium"] = res_6m

    # ---------------------------------------------------------
    # n = 8 (with further restricted arities)
    # ---------------------------------------------------------
    n = 8
    print(f"\n{'#'*80}")
    print(f"# BLOCK 3: n = {n}")
    print(f"{'#'*80}")

    clauses_8 = make_sparse_2sat(n, seed=20)
    arities_8 = [3, 5, 7, 9]
    res_8 = run_instance_test(n, clauses_8, f"n={n} sparse 2-SAT",
                               arities=arities_8)
    if res_8:
        all_results["n8_sparse"] = res_8

    clauses_8m = make_medium_2sat(n, seed=21)
    res_8m = run_instance_test(n, clauses_8m, f"n={n} medium 2-SAT",
                                arities=arities_8)
    if res_8m:
        all_results["n8_medium"] = res_8m

    # ---------------------------------------------------------
    # Cross-polymorphism tests
    # ---------------------------------------------------------
    print(f"\n{'#'*80}")
    print(f"# BLOCK 4: Cross-polymorphism tests")
    print(f"{'#'*80}")

    # Use n=4 sparse instance for cross-polymorphism
    cross_res_1 = run_cross_polymorphism_test(
        4, make_sparse_2sat(4, seed=0), "n=4 sparse (maj vs pi_2)"
    )
    if cross_res_1:
        all_results["cross_n4_sparse"] = cross_res_1

    cross_res_2 = run_cross_polymorphism_test(
        4, make_trivial_instance(4), "n=4 trivial (maj vs pi_2)"
    )
    if cross_res_2:
        all_results["cross_n4_trivial"] = cross_res_2

    # ---------------------------------------------------------
    # Global summary
    # ---------------------------------------------------------
    print(f"\n{'='*80}")
    print(f"GLOBAL SUMMARY")
    print(f"{'='*80}")

    print(f"\n  Instances tested: {len(all_results)}")

    # Check: does d_PU(U_{f_k}, scalar) stay bounded below?
    print(f"\n  --- Non-scalarity (d_PU to scalar) across all instances ---")
    for key, res in all_results.items():
        if "scalar_PU_dist_op" in res:
            dists = res["scalar_PU_dist_op"]
            if len(dists) > 0:
                mn = min(dists)
                mx = max(dists)
                trend = "DECREASING" if len(dists) > 1 and dists[-1] < dists[0] else "STABLE/INCREASING"
                print(f"  {key}: min={mn:.6f}, max={mx:.6f}, "
                      f"trend={trend}, last={dists[-1]:.6f}")

    # Check: does d_PU(consecutive) stay bounded below?
    print(f"\n  --- Consecutive PU-separation across all instances ---")
    for key, res in all_results.items():
        if "consecutive_PU_dist_op" in res:
            dists = res["consecutive_PU_dist_op"]
            if len(dists) > 0:
                mn = min(dists)
                mx = max(dists)
                print(f"  {key}: min={mn:.6f}, max={mx:.6f}, "
                      f"last={dists[-1]:.6f}")

    # ---------------------------------------------------------
    # FINAL VERDICTS
    # ---------------------------------------------------------
    print(f"\n{'='*80}")
    print(f"FINAL VERDICTS FOR LEMMA 2.6.4 REPAIR")
    print(f"{'='*80}")

    # Collect all scalar distances
    all_scalar_dists = []
    for key, res in all_results.items():
        if "scalar_PU_dist_op" in res:
            all_scalar_dists.extend(res["scalar_PU_dist_op"])

    # Collect all consecutive distances
    all_consec_dists = []
    for key, res in all_results.items():
        if "consecutive_PU_dist_op" in res:
            all_consec_dists.extend(res["consecutive_PU_dist_op"])

    if all_scalar_dists:
        global_min_scalar = min(all_scalar_dists)
        print(f"\n  1. NON-SCALARITY: min d_PU(U_{{f_k}}, scalar) "
              f"across all instances and arities = {global_min_scalar:.8f}")
        if global_min_scalar > 0.001:
            print(f"     VERDICT: NON-SCALARITY HOLDS -- "
                  f"the polymorphism unitaries do NOT approach scalars.")
            print(f"     The unitary U_{{f_k}} stays at least "
                  f"{global_min_scalar:.6f} away from cI at every tested "
                  f"instance and arity.")
        elif global_min_scalar < 1e-6:
            print(f"     VERDICT: NON-SCALARITY FAILS -- "
                  f"the unitaries collapse to scalars at high arity.")
        else:
            print(f"     VERDICT: MARGINAL -- values are small. "
                  f"Need higher arities to determine trend.")

    if all_consec_dists:
        global_min_consec = min(all_consec_dists)
        print(f"\n  2. INSTANCE DIVERSITY (consecutive-arity separation):")
        print(f"     min d_PU(U_{{k}}, U_{{k+2}}) = {global_min_consec:.8f}")
        if global_min_consec > 0.001:
            print(f"     VERDICT: CONSECUTIVE-ARITY SEPARATION HOLDS -- "
                  f"different arities give PU-separated unitaries.")
        elif global_min_consec < 1e-6:
            print(f"     VERDICT: CONSECUTIVE-ARITY SEPARATION VANISHES -- "
                  f"the unitaries converge as k grows.")
        else:
            print(f"     VERDICT: MARGINAL")

    print(f"\n  3. OVERALL VERDICT FOR LEMMA 2.6.4:")
    if all_scalar_dists and all_consec_dists:
        if min(all_scalar_dists) > 0.001 and min(all_consec_dists) > 0.001:
            print(f"     GAP CLOSED: Both non-scalarity and consecutive "
                  f"separation hold.")
            print(f"     The Critic's concern (separation vanishing as k "
                  f"grows) is NOT observed.")
            print(f"     The instance diversity lemma is empirically "
                  f"validated at these scales.")
        elif min(all_scalar_dists) > 0.001 and min(all_consec_dists) < 0.001:
            print(f"     PARTIAL: Non-scalarity holds but consecutive "
                  f"separation shrinks.")
            print(f"     Lemma 2.6.4 needs refinement: the separation is "
                  f"between polymorphism and scalar,")
            print(f"     not necessarily between consecutive arities.")
        elif min(all_scalar_dists) < 0.001:
            print(f"     GAP NOT CLOSED: Non-scalarity fails. "
                  f"The Critic was right.")
            print(f"     Lemma 2.6.4 needs a different witness instance "
                  f"strategy.")
        else:
            print(f"     INCONCLUSIVE: Need larger arities or larger instances.")

    # Save results
    results_path = ("/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/"
                    "clone-growth-fullness-bridge/code/"
                    "instance_diversity_results.json")
    # Convert to JSON-serializable format
    json_results = {}
    for key, res in all_results.items():
        jr = {}
        for k, v in res.items():
            if isinstance(v, dict):
                jr[k] = {}
                for k2, v2 in v.items():
                    if isinstance(v2, dict):
                        jr[k][k2] = {
                            k3: (v3 if not isinstance(v3, complex)
                                 else str(v3))
                            for k3, v3 in v2.items()
                        }
                    else:
                        jr[k][k2] = v2
            elif isinstance(v, np.ndarray):
                jr[k] = v.tolist()
            elif isinstance(v, (np.floating, np.integer)):
                jr[k] = float(v)
            else:
                jr[k] = v
        json_results[key] = jr

    with open(results_path, "w") as f:
        json.dump(json_results, f, indent=2, default=str)
    print(f"\n  Results saved to: {results_path}")


if __name__ == "__main__":
    main()
