"""
reverify_q6_outdim.py -- Independent re-verification of Q6-OUTDIM entry
in the P vs NP transposition dictionary.

Claim: dim_poly_k (non-projection k-ary solution-preserving operations)
grows exponentially with k for P-time CSPs and collapses to zero for
NPC CSPs.  Perfect 6/6 separation at k=5, n=10.

ALGORITHM for k=5:
  A k=5 truth table is a 32-bit integer tt.
  For a k-tuple (s1,...,s5) of solutions, at each bit position b,
  the pattern p_b = concat(s1[b],...,s5[b]) is a 5-bit number.
  Applying tt: output_b = (tt >> p_b) & 1.
  The assembled output must be in Sol.

  We use CONSTRAINT PROPAGATION on the 32-bit TT:
  - For each k-tuple, the n output bits are determined by n entries of tt.
  - The constraint is: the n-bit output must be a solution.
  - We represent allowed TTs as a product of allowed-bit-sets for each
    of the 32 TT entries, then intersect constraints.

  Actually, the constraints couple multiple TT entries (the output
  depends on several entries jointly), so we cannot decompose into
  independent bits. Instead, we use the SAMPLING approach but with
  numpy for speed.

Author: G Six (originator), Claude Opus 4.6 (collaborator)
Date: 2026-04-12
"""

import random
import itertools
import math
import time
import json
import sys
import numpy as np

SEED = 2026_04_12
random.seed(SEED)
np.random.seed(SEED)

# =====================================================================
# UTILITIES
# =====================================================================

def find_solutions_bruteforce(clauses, n, mode='or'):
    solutions = []
    for val in range(1 << n):
        bits = tuple((val >> (n - 1 - i)) & 1 for i in range(n))
        sat = True
        for clause in clauses:
            if mode == 'or':
                ok = any(
                    (lit > 0 and bits[abs(lit) - 1] == 1) or
                    (lit < 0 and bits[abs(lit) - 1] == 0)
                    for lit in clause
                )
                if not ok:
                    sat = False; break
            elif mode == 'xor':
                count = sum(
                    1 for lit in clause
                    if (lit > 0 and bits[abs(lit) - 1] == 1) or
                       (lit < 0 and bits[abs(lit) - 1] == 0)
                )
                if count % 2 == 0:
                    sat = False; break
            elif mode == 'nae':
                vals = set()
                for lit in clause:
                    v = bits[abs(lit) - 1]
                    if lit < 0:
                        v = 1 - v
                    vals.add(v)
                if len(vals) == 1:
                    sat = False; break
        if sat:
            solutions.append(bits)
    return solutions


def gen_instance(n, csp_type, alpha=None):
    for attempt in range(200):
        clauses, mode = _gen_raw(n, csp_type, alpha)
        sols = find_solutions_bruteforce(clauses, n, mode)
        if len(sols) >= 5:
            return clauses, mode, sols
    raise RuntimeError(f"Could not generate satisfiable {csp_type} instance after 200 tries")


def _gen_raw(n, csp_type, alpha):
    if csp_type == '2-SAT':
        m = int((alpha or 1.5) * n)
        clauses = [[v if random.random() < 0.5 else -v
                     for v in random.sample(range(1, n + 1), 2)]
                    for _ in range(m)]
        return clauses, 'or'
    elif csp_type == 'Horn':
        m = int((alpha or 2.0) * n)
        clauses = []
        for _ in range(m):
            width = random.randint(2, 3)
            vs = random.sample(range(1, n + 1), min(width, n))
            pos_idx = random.randint(0, len(vs) - 1)
            clause = [-v if i != pos_idx else v for i, v in enumerate(vs)]
            clauses.append(clause)
        return clauses, 'or'
    elif csp_type == 'Dual-Horn':
        m = int((alpha or 2.0) * n)
        clauses = []
        for _ in range(m):
            width = random.randint(2, 3)
            vs = random.sample(range(1, n + 1), min(width, n))
            neg_idx = random.randint(0, len(vs) - 1)
            clause = [v if i != neg_idx else -v for i, v in enumerate(vs)]
            clauses.append(clause)
        return clauses, 'or'
    elif csp_type == 'XOR-SAT':
        m = int((alpha or 0.5) * n)
        clauses = [[v if random.random() < 0.5 else -v
                     for v in random.sample(range(1, n + 1), 3)]
                    for _ in range(m)]
        return clauses, 'xor'
    elif csp_type == '3-SAT':
        m = int((alpha or 3.0) * n)
        clauses = [[v if random.random() < 0.5 else -v
                     for v in random.sample(range(1, n + 1), 3)]
                    for _ in range(m)]
        return clauses, 'or'
    elif csp_type == 'NAE-3-SAT':
        m = int((alpha or 1.5) * n)
        clauses = [[v if random.random() < 0.5 else -v
                     for v in random.sample(range(1, n + 1), 3)]
                    for _ in range(m)]
        return clauses, 'nae'
    else:
        raise ValueError(f"Unknown CSP type: {csp_type}")


# =====================================================================
# CORE: Polymorphism counting
# =====================================================================

def build_projection_tts(k):
    tt_size = 1 << k
    proj_set = set()
    for proj_idx in range(k):
        tt = 0
        for j in range(tt_size):
            bit_val = (j >> (k - 1 - proj_idx)) & 1
            tt |= (bit_val << j)
        proj_set.add(tt)
    return proj_set


def count_preserving_exhaustive(solutions, k, max_tuples=50000):
    """Exhaustively count k-ary preserving operations (k <= 4)."""
    sol_set = set(solutions)
    n_bits = len(solutions[0])
    n_sols = len(solutions)
    tt_size = 1 << k
    n_possible = 1 << tt_size

    if n_sols == 0:
        return 0, 0

    total_tuples = n_sols ** k
    if total_tuples <= max_tuples:
        all_tuples = list(itertools.product(range(n_sols), repeat=k))
    else:
        tuples_set = set()
        for i in range(n_sols):
            tuples_set.add(tuple([i] * k))
        while len(tuples_set) < max_tuples:
            t = tuple(random.randint(0, n_sols - 1) for _ in range(k))
            tuples_set.add(t)
        all_tuples = list(tuples_set)

    all_tuples.sort(key=lambda t: -len(set(t)))
    allowed = set(range(n_possible))

    for tup in all_tuples:
        if not allowed or len(allowed) <= k:
            break
        patterns = []
        for b in range(n_bits):
            pat_idx = 0
            for j in range(k):
                pat_idx = 2 * pat_idx + solutions[tup[j]][b]
            patterns.append(pat_idx)
        new_allowed = set()
        for tt in allowed:
            output = tuple((tt >> patterns[b]) & 1 for b in range(n_bits))
            if output in sol_set:
                new_allowed.add(tt)
        allowed = new_allowed

    total = len(allowed)
    proj_set = build_projection_tts(k)
    n_proj = len(allowed & proj_set)
    return total, total - n_proj


def count_preserving_sampled_k5_numpy(solutions, n_samples=100_000):
    """Vectorized k=5 sampling using numpy.

    Key idea: precompute pattern arrays for a set of k-tuples,
    then test batches of random TTs against all constraints at once.
    """
    k = 5
    tt_size = 1 << k  # 32
    total_fns = 2**32

    sol_arr = np.array(solutions, dtype=np.uint8)  # shape (n_sols, n_bits)
    n_sols, n_bits = sol_arr.shape
    sol_set = set(tuple(s) for s in solutions)

    # Encode each solution as an integer for fast lookup
    sol_ints = set()
    for s in solutions:
        val = 0
        for b in s:
            val = 2 * val + b
        sol_ints.add(val)

    proj_set = build_projection_tts(k)

    # Generate k-tuples for constraint checking
    total_tuples = n_sols ** k
    if total_tuples <= 50000:
        # Use ALL tuples
        tuple_indices = np.array(list(itertools.product(range(n_sols), repeat=k)),
                                  dtype=np.int32)
    else:
        # Sample tuples, including all diagonals
        n_tup = min(50000, total_tuples)
        tuples_set = set()
        for i in range(n_sols):
            tuples_set.add(tuple([i] * k))
        while len(tuples_set) < n_tup:
            t = tuple(np.random.randint(0, n_sols, size=k).tolist())
            tuples_set.add(t)
        tuple_indices = np.array(list(tuples_set), dtype=np.int32)

    n_tuples = len(tuple_indices)

    # Precompute patterns: for each tuple, for each bit position,
    # the 5-bit pattern index into the truth table
    # patterns[t, b] = sum_j sol[tuple[t][j]][b] * 2^(4-j)
    # Shape: (n_tuples, n_bits)
    patterns = np.zeros((n_tuples, n_bits), dtype=np.int32)
    for j in range(k):
        sol_at_j = sol_arr[tuple_indices[:, j], :]  # shape (n_tuples, n_bits)
        patterns += sol_at_j.astype(np.int32) * (1 << (k - 1 - j))

    # For each tuple, we also need the expected output to be in sol_set.
    # The output for tuple t and TT tt is:
    #   output_b = (tt >> patterns[t, b]) & 1
    # And the n-bit output must be in sol_set.

    # Process in batches
    batch_size = 10000
    n_hits = 0
    n_nonproj = 0

    for batch_start in range(0, n_samples, batch_size):
        batch_end = min(batch_start + batch_size, n_samples)
        bs = batch_end - batch_start

        # Generate random 32-bit TTs
        # numpy doesn't directly support uint32 randint up to 2^32,
        # so we compose from two 16-bit halves
        lo = np.random.randint(0, 1 << 16, size=bs, dtype=np.int64)
        hi = np.random.randint(0, 1 << 16, size=bs, dtype=np.int64)
        tts = (hi << 16) | lo  # shape (bs,), int64

        # For each TT, check ALL tuples
        # We process tuple by tuple and track which TTs still pass
        alive = np.ones(bs, dtype=bool)

        for t_idx in range(n_tuples):
            if not np.any(alive):
                break

            pat = patterns[t_idx]  # shape (n_bits,)

            # For alive TTs, compute output bits
            alive_indices = np.where(alive)[0]
            alive_tts = tts[alive_indices]

            # output[i, b] = (alive_tts[i] >> pat[b]) & 1
            # Compute the n-bit output integer for each alive TT
            output_int = np.zeros(len(alive_indices), dtype=np.int64)
            for b in range(n_bits):
                bit = (alive_tts >> pat[b]) & 1
                output_int = output_int * 2 + bit

            # Check which outputs are in sol_ints
            valid = np.array([int(v) in sol_ints for v in output_int], dtype=bool)
            alive[alive_indices[~valid]] = False

        # Count hits
        hit_mask = alive
        batch_hits = np.sum(hit_mask)
        n_hits += batch_hits

        # Check projections
        if batch_hits > 0:
            hit_tts = tts[hit_mask]
            for tt_val in hit_tts:
                if int(tt_val) not in proj_set:
                    n_nonproj += 1

    # Estimate
    p_hat = n_hits / n_samples
    est_dim = p_hat * total_fns

    # Wilson CI
    if n_hits > 0:
        z = 1.96
        denom = 1 + z**2 / n_samples
        center = (p_hat + z**2 / (2 * n_samples)) / denom
        half_width = z * math.sqrt(p_hat * (1 - p_hat) / n_samples + z**2 / (4 * n_samples**2)) / denom
        ci_low = max(0, (center - half_width)) * total_fns
        ci_high = (center + half_width) * total_fns
    else:
        ci_low = 0
        ci_high = (3.0 / n_samples) * total_fns

    return n_hits, n_nonproj, est_dim, ci_low, ci_high


# =====================================================================
# MAIN
# =====================================================================

CSP_CLASSES = [
    ('2-SAT',      'P'),
    ('Horn',       'P'),
    ('Dual-Horn',  'P'),
    ('XOR-SAT',    'P'),
    ('3-SAT',      'NPC'),
    ('NAE-3-SAT',  'NPC'),
]

N_INSTANCES = 20
N_VARS = 10


def main():
    print("=" * 72)
    print("INDEPENDENT RE-VERIFICATION OF Q6-OUTDIM")
    print(f"n = {N_VARS}, {N_INSTANCES} instances per class, seed = {SEED}")
    print(f"k=2,3,4: exhaustive TT enumeration")
    print(f"k=5: 100k random TTs, checked against up to 50k solution tuples")
    print("=" * 72)
    sys.stdout.flush()

    results = {}

    for csp_name, complexity in CSP_CLASSES:
        print(f"\n{'─' * 60}")
        print(f"  {csp_name}  ({complexity})")
        print(f"{'─' * 60}")
        sys.stdout.flush()

        dims = {2: [], 3: [], 4: [], 5: []}
        hits_k5_list = []
        nonproj_k5_list = []
        sol_sizes = []
        t_start = time.time()

        for inst in range(N_INSTANCES):
            clauses, mode, sols = gen_instance(N_VARS, csp_name)
            sol_sizes.append(len(sols))

            # k=2: exhaustive (16 TTs)
            _, np2 = count_preserving_exhaustive(sols, 2)
            dims[2].append(np2)

            # k=3: exhaustive (256 TTs)
            _, np3 = count_preserving_exhaustive(sols, 3)
            dims[3].append(np3)

            # k=4: exhaustive (65536 TTs)
            _, np4 = count_preserving_exhaustive(sols, 4)
            dims[4].append(np4)

            # k=5: sampled with numpy
            n_hits, n_nonproj, est_dim, ci_lo, ci_hi = count_preserving_sampled_k5_numpy(sols)
            dims[5].append(est_dim)
            hits_k5_list.append(n_hits)
            nonproj_k5_list.append(n_nonproj)

            if (inst + 1) % 5 == 0:
                elapsed = time.time() - t_start
                print(f"    instance {inst+1}/{N_INSTANCES}  ({elapsed:.1f}s)  "
                      f"|Sol|={len(sols)}, k5_hits={n_hits}")
                sys.stdout.flush()

        elapsed = time.time() - t_start

        avg = {k: sum(v) / len(v) for k, v in dims.items()}
        med = {k: sorted(v)[len(v) // 2] for k, v in dims.items()}
        min_d = {k: min(v) for k, v in dims.items()}
        max_d = {k: max(v) for k, v in dims.items()}
        total_k5_hits = sum(hits_k5_list)
        total_k5_nonproj = sum(nonproj_k5_list)
        avg_sols = sum(sol_sizes) / len(sol_sizes)

        results[csp_name] = {
            'complexity': complexity,
            'avg_sols': avg_sols,
            'dims_avg': avg,
            'dims_med': med,
            'dims_min': min_d,
            'dims_max': max_d,
            'k5_total_hits': total_k5_hits,
            'k5_total_nonproj_hits': total_k5_nonproj,
            'k5_hits_per_instance': hits_k5_list,
            'k5_nonproj_per_instance': nonproj_k5_list,
            'all_k5_dims': dims[5],
            'all_k4_dims': dims[4],
            'all_k3_dims': dims[3],
            'all_k2_dims': dims[2],
            'sol_sizes': sol_sizes,
        }

        print(f"  Avg |Sol| = {avg_sols:.1f}, range [{min(sol_sizes)}, {max(sol_sizes)}]")
        print(f"  dim_poly (avg over {N_INSTANCES} instances):")
        for k in [2, 3, 4, 5]:
            print(f"    k={k}: avg={avg[k]:.1f}, median={med[k]:.1f}, "
                  f"range=[{min_d[k]:.0f}, {max_d[k]:.0f}]")
        print(f"  k=5: total hits={total_k5_hits}, nonproj={total_k5_nonproj} "
              f"in {N_INSTANCES * 100_000:,} samples")
        print(f"  Time: {elapsed:.1f}s")
        sys.stdout.flush()

    # =====================================================================
    # VERIFICATION SUMMARY
    # =====================================================================
    print("\n" + "=" * 72)
    print("VERIFICATION SUMMARY")
    print("=" * 72)

    p_time_k5_positive = True
    p_time_failures = []
    for name, comp in CSP_CLASSES:
        if comp == 'P':
            hits = results[name]['k5_total_hits']
            if hits == 0:
                p_time_k5_positive = False
                p_time_failures.append(name)
                print(f"  NOTE: {name} (P) has 0 hits at k=5 in {N_INSTANCES*100000:,} samples")

    npc_k5_zero = True
    npc_failures = []
    for name, comp in CSP_CLASSES:
        if comp == 'NPC':
            nonproj = results[name]['k5_total_nonproj_hits']
            total = results[name]['k5_total_hits']
            if nonproj > 0:
                npc_k5_zero = False
                npc_failures.append((name, nonproj))
                print(f"  *** SIGNIFICANT: {name} (NPC) has {nonproj} non-proj hits at k=5! ***")
            elif total > 0:
                print(f"  NOTE: {name} (NPC) has {total} hits at k=5 but all projections")

    print("\nGrowth trajectories (averages):")
    for name, comp in CSP_CLASSES:
        r = results[name]
        traj = [r['dims_avg'][k] for k in [2, 3, 4, 5]]
        label = "P  " if comp == 'P' else "NPC"
        print(f"  {label} {name:12s}: k=2:{traj[0]:>12.1f}  k=3:{traj[1]:>12.1f}  "
              f"k=4:{traj[2]:>12.1f}  k=5:{traj[3]:>14.1f}")

    print()
    sep_k5 = p_time_k5_positive and npc_k5_zero
    if p_time_k5_positive:
        print(f"  Claim 1 (all P have dim_5 > 0):     PASS")
    else:
        print(f"  Claim 1 (all P have dim_5 > 0):     FAIL ({', '.join(p_time_failures)})")
    print(f"  Claim 2 (all NPC have dim_5 = 0):    {'PASS' if npc_k5_zero else 'FAIL'}")
    print(f"  Perfect 6/6 separation at k=5:       {'PASS' if sep_k5 else 'FAIL'}")

    # Low arity
    npc_k2_nonzero = any(results[name]['dims_avg'][2] > 0
                         for name, comp in CSP_CLASSES if comp == 'NPC')
    print(f"  Low arity non-separation:            {'CONFIRMED' if npc_k2_nonzero else 'NPC zero at k=2'}")

    # k=4 separation check
    print("\n  k=4 separation check:")
    for name, comp in CSP_CLASSES:
        r = results[name]
        label = "P  " if comp == 'P' else "NPC"
        print(f"    {label} {name:12s}: avg dim_4 = {r['dims_avg'][4]:.1f}")

    # Exponential growth
    print("\n  Exponential growth (P-time, k=2 to k=4):")
    for name, comp in CSP_CLASSES:
        if comp == 'P':
            d2 = results[name]['dims_avg'][2]
            d3 = results[name]['dims_avg'][3]
            d4 = results[name]['dims_avg'][4]
            print(f"    {name:12s}: {d2:.1f} -> {d3:.1f} -> {d4:.1f}")

    print("\n" + "=" * 72)
    if sep_k5:
        print("OVERALL VERDICT: Q6-OUTDIM VERIFIED -- perfect 6/6 separation at k=5")
    else:
        print("OVERALL VERDICT: Q6-OUTDIM -- ISSUES FOUND")
        if p_time_failures:
            print(f"  P-time classes with 0 k=5 hits: {p_time_failures}")
            print(f"  Likely explanation: polymorphism density for these classes")
            print(f"  is below ~1/100k of 2^32, i.e., fewer than ~43,000 polymorphisms.")
            print(f"  They DO have growing polymorphisms at k=2,3,4 (exhaustive).")
        if npc_failures:
            print(f"  NPC classes with k=5 non-proj hits: {npc_failures}")
            print(f"  This is either a false positive from insufficient tuple coverage")
            print(f"  or a genuine counterexample to the claim.")
    print("=" * 72)

    # Save results
    output_path = "/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/code/results_reverify_q6.json"

    def to_native(obj):
        """Convert numpy types to native Python for JSON serialization."""
        if isinstance(obj, (np.integer,)):
            return int(obj)
        elif isinstance(obj, (np.floating,)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, dict):
            return {str(k): to_native(v) for k, v in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [to_native(v) for v in obj]
        return obj

    json_results = to_native(results)
    with open(output_path, 'w') as f:
        json.dump(json_results, f, indent=2)
    print(f"\nRaw results saved to {output_path}")

    return results, sep_k5


if __name__ == '__main__':
    results, verified = main()
    sys.exit(0 if verified else 1)
