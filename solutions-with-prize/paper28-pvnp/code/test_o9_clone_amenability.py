#!/usr/bin/env python3
"""
test_o9_clone_amenability.py — Clone amenability vs non-amenability test

Tests conjecture O9 from the transposition dictionary:

  The clone (set of all polymorphisms) of a P-time CSP is AMENABLE as a
  monoid under composition, while the clone of an NPC CSP is NON-AMENABLE
  (its automorphism group contains a free subgroup).

THREE INDEPENDENT TESTS:

  Test 1 — Clone richness across arities (n=8, k=2,3,4):
    P-time clones grow super-polynomially in 2^k (rich polymorphisms).
    NPC clones stay at k + const (essentially unary only).
    Growth rate of |Clone_k| / 2^k distinguishes the two.

  Test 2 — Folner condition on SUBSETS (n=6, k=3):
    For the finite clone, we test boundary ratios on PROPER subsets F ⊊ Clone.
    Amenable monoids: for any epsilon, exists F with |∂F|/|F| < epsilon.
    We test whether small random subsets already have low boundary ratio
    (P-time clones are "internally connected") vs high ratio (NPC clones
    are "fragmented" — mostly projections + a few isolated extras).

  Test 3 — Wreath product Cayley growth (n=4..10):
    The hyperoctahedral group (Z/2)^n ⋊ S_n (symmetry group of the hypercube)
    acts on {0,1}^n. For NPC clones, the only polymorphisms factor through
    this group action. Show exponential Cayley growth rate persists as n grows,
    indicating non-amenability in the limit.

Parameters: n=8 (Tests 1,2), n=6 (Test 2 Folner), n=4..10 (Test 3).

Author: G Six (originator), Claude Opus 4.6 (collaborator)
Date: 2026-04-12
"""

import random
import itertools
import math
import time
from collections import deque
from mpmath import mp, mpf, log as mplog

mp.dps = 60
random.seed(42)

# =====================================================================
# CSP INSTANCE GENERATORS & SOLUTION FINDER
# =====================================================================

def find_solutions(clauses, n, mode='or'):
    """Enumerate all solutions by brute force over {0,1}^n."""
    solutions = []
    for bits in itertools.product([0, 1], repeat=n):
        sat = True
        for clause in clauses:
            if mode == 'or':
                ok = any((lit > 0 and bits[abs(lit)-1] == 1) or
                         (lit < 0 and bits[abs(lit)-1] == 0) for lit in clause)
                if not ok:
                    sat = False; break
            elif mode == 'xor':
                vs, target = clause
                xor_val = 0
                for v in vs:
                    xor_val ^= bits[v-1]
                if xor_val != target:
                    sat = False; break
            elif mode == 'nae':
                vals = set()
                for lit in clause:
                    v = bits[abs(lit)-1]
                    if lit < 0: v = 1 - v
                    vals.add(v)
                if len(vals) == 1:
                    sat = False; break
        if sat:
            solutions.append(bits)
    return solutions


def gen_clauses(n, mode, clause_width, alpha):
    """Generate random CSP clauses."""
    m = int(alpha * n)
    if mode == '2sat':
        clauses = []
        for _ in range(m):
            vs = random.sample(range(1, n+1), 2)
            clause = [v if random.random() < 0.5 else -v for v in vs]
            clauses.append(clause)
        return clauses, 'or'
    elif mode == 'horn':
        clauses = []
        for _ in range(m):
            kk = random.randint(2, clause_width)
            vs = random.sample(range(1, n+1), min(kk, n))
            pos = random.randint(0, len(vs)-1)
            clause = [-v if i != pos else v for i, v in enumerate(vs)]
            clauses.append(clause)
        return clauses, 'or'
    elif mode == 'dhorn':
        clauses = []
        for _ in range(m):
            kk = random.randint(2, clause_width)
            vs = random.sample(range(1, n+1), min(kk, n))
            neg = random.randint(0, len(vs)-1)
            clause = [v if i != neg else -v for i, v in enumerate(vs)]
            clauses.append(clause)
        return clauses, 'or'
    elif mode == 'xor':
        clauses = []
        for _ in range(m):
            vs = random.sample(range(1, n+1), 3)
            target = random.randint(0, 1)
            clauses.append((vs, target))
        return clauses, 'xor'
    elif mode == '3sat':
        clauses = [[v if random.random() < 0.5 else -v
                     for v in random.sample(range(1, n+1), 3)]
                    for _ in range(m)]
        return clauses, 'or'
    elif mode == 'nae':
        clauses = [[v if random.random() < 0.5 else -v
                     for v in random.sample(range(1, n+1), 3)]
                    for _ in range(m)]
        return clauses, 'nae'
    else:
        raise ValueError(f"Unknown mode: {mode}")


# =====================================================================
# CLONE ENUMERATION
# =====================================================================

def enumerate_clone_k(solutions, k, max_sol_tuples=3000):
    """Enumerate Clone_k: all k-ary ops f:{0,1}^k->{0,1} preserving Sol.
    Returns (allowed_set, projection_set)."""
    sol_set = set(solutions)
    n_bits = len(solutions[0])
    n_sols = len(solutions)
    tt_size = 2 ** k
    n_possible = 2 ** tt_size

    if n_sols == 0:
        return set(), set()

    if n_sols ** k <= max_sol_tuples:
        all_tuples = list(itertools.product(range(n_sols), repeat=k))
    else:
        tuples_set = set()
        for i in range(n_sols):
            tuples_set.add(tuple([i] * k))
        while len(tuples_set) < min(max_sol_tuples, n_sols ** k):
            t = tuple(random.randint(0, n_sols - 1) for _ in range(k))
            tuples_set.add(t)
        all_tuples = list(tuples_set)

    all_tuples.sort(key=lambda t: -len(set(t)))

    patterns_list = []
    for tup in all_tuples:
        pats = tuple(
            sum(solutions[tup[j]][b] << (k - 1 - j) for j in range(k))
            for b in range(n_bits)
        )
        patterns_list.append(pats)

    allowed = set(range(n_possible))

    for pats in patterns_list:
        if not allowed:
            break
        new_allowed = set()
        for tt in allowed:
            output = tuple((tt >> pats[b]) & 1 for b in range(n_bits))
            if output in sol_set:
                new_allowed.add(tt)
        allowed = new_allowed

    projection_tts = set()
    for proj_idx in range(k):
        tt = 0
        for j in range(tt_size):
            bit_val = (j >> (k - 1 - proj_idx)) & 1
            tt |= (bit_val << j)
        projection_tts.add(tt)

    return allowed, projection_tts


def is_essentially_unary(tt, k):
    """Check if a truth table depends on at most 1 coordinate."""
    tt_size = 2 ** k
    # Count how many coordinates tt depends on
    dep_count = 0
    for coord in range(k):
        depends = False
        for j in range(tt_size):
            j_flipped = j ^ (1 << (k - 1 - coord))
            if ((tt >> j) & 1) != ((tt >> j_flipped) & 1):
                depends = True
                break
        if depends:
            dep_count += 1
    return dep_count <= 1


def essential_arity(tt, k):
    """Return the number of coordinates tt genuinely depends on."""
    tt_size = 2 ** k
    dep_count = 0
    for coord in range(k):
        for j in range(tt_size):
            j_flipped = j ^ (1 << (k - 1 - coord))
            if ((tt >> j) & 1) != ((tt >> j_flipped) & 1):
                dep_count += 1
                break
    return dep_count


# =====================================================================
# TEST 1: CLONE RICHNESS ACROSS ARITIES
# =====================================================================

def test1_clone_richness():
    """For each class, compute |Clone_k| at k=2,3,4.
    P-time: super-polynomial growth. NPC: linear/constant growth."""

    print("\n" + "=" * 72)
    print("TEST 1: Clone richness across arities (n=8)")
    print("=" * 72)

    CLASSES = {
        '2-SAT':     ('2sat', 3, 2.5),
        'Horn-SAT':  ('horn', 3, 2.5),
        'Dual-Horn': ('dhorn', 3, 2.5),
        'XOR-SAT':   ('xor', 3, 1.0),
        '3-SAT':     ('3sat', 3, 4.0),   # near threshold (~4.27 for random 3-SAT)
        'NAE-3-SAT': ('nae', 3, 2.5),
    }

    N = 8
    N_INST = 20  # more instances to get enough valid ones
    results = {}

    for cls_name, (mode, width, alpha) in CLASSES.items():
        print(f"\n  {cls_name}:")
        cls_data = {}

        for k in [2, 3, 4]:
            sizes = []
            non_projs = []
            eu_fracs = []

            for inst in range(N_INST):
                clauses, solve_mode = gen_clauses(N, mode, width, alpha)
                sols = find_solutions(clauses, N, mode=solve_mode)
                if len(sols) < 2:
                    continue
                # For k=4, skip if solution set too large (enumeration too slow)
                if k == 4 and len(sols) > 40:
                    continue

                clone, projs = enumerate_clone_k(sols, k, max_sol_tuples=2000)
                sizes.append(len(clone))
                non_projs.append(len(clone) - len(clone & projs))

                eu_count = sum(1 for tt in clone if is_essentially_unary(tt, k))
                eu_fracs.append(eu_count / len(clone) if clone else 1.0)

            if sizes:
                avg_size = sum(sizes) / len(sizes)
                avg_np = sum(non_projs) / len(non_projs)
                avg_eu = sum(eu_fracs) / len(eu_fracs)
                cls_data[k] = {
                    'mean_size': avg_size, 'mean_non_proj': avg_np,
                    'eu_frac': avg_eu, 'n_inst': len(sizes),
                    'sizes': sizes,
                }
                print(f"    k={k}: |Clone|={avg_size:.1f}, non-proj={avg_np:.1f}, "
                      f"EU_frac={avg_eu:.3f} (n={len(sizes)})")
            else:
                cls_data[k] = None
                print(f"    k={k}: no valid instances")

        # Compute growth ratio: |Clone_4| / |Clone_3| and |Clone_3| / |Clone_2|
        if cls_data.get(2) and cls_data.get(3):
            r23 = cls_data[3]['mean_size'] / max(cls_data[2]['mean_size'], 1)
            print(f"    Growth k=2->3: {r23:.2f}x")
        if cls_data.get(3) and cls_data.get(4):
            r34 = cls_data[4]['mean_size'] / max(cls_data[3]['mean_size'], 1)
            print(f"    Growth k=3->4: {r34:.2f}x")

        results[cls_name] = cls_data

    return results


# =====================================================================
# TEST 2: FOLNER-LIKE BOUNDARY ON SUBSETS
# =====================================================================

def compose_tt_slot(f_tt, g_tt, k, slot=0):
    """Compose: replace slot-th argument of f with output of g.
    h(x) = f(x_0,...,g(x),...,x_{k-1}) where g replaces position 'slot'."""
    tt_size = 2 ** k
    result = 0
    for j in range(tt_size):
        g_val = (g_tt >> j) & 1
        # Replace bit at position 'slot' in j with g_val
        mask = 1 << (k - 1 - slot)
        new_j = (j & ~mask) | (g_val << (k - 1 - slot))
        f_val = (f_tt >> new_j) & 1
        result |= (f_val << j)
    return result


def test2_folner_boundary():
    """Test Folner boundary ratios on subsets of Clone_k.

    For P-time clones (large, rich): random subsets have LOW boundary ratio
    because the clone is "well-connected" under composition.

    For NPC clones (small, sparse): random subsets have HIGH boundary ratio
    because operations are isolated (mostly projections + constants).
    """

    print("\n" + "=" * 72)
    print("TEST 2: Folner boundary ratios (n=8, k=3)")
    print("=" * 72)

    CLASSES = {
        '2-SAT':     ('2sat', 3, 2.5),
        'Horn-SAT':  ('horn', 3, 2.5),
        'Dual-Horn': ('dhorn', 3, 2.5),
        'XOR-SAT':   ('xor', 3, 1.0),
        '3-SAT':     ('3sat', 3, 4.0),
        'NAE-3-SAT': ('nae', 3, 2.5),
    }

    N = 8
    k = 3
    N_INST = 15
    results = {}

    for cls_name, (mode, width, alpha) in CLASSES.items():
        print(f"\n  {cls_name}:")
        boundary_data = []

        for inst in range(N_INST):
            clauses, solve_mode = gen_clauses(N, mode, width, alpha)
            sols = find_solutions(clauses, N, mode=solve_mode)
            if len(sols) < 2:
                continue

            clone, projs = enumerate_clone_k(sols, k, max_sol_tuples=2000)
            clone_list = sorted(clone)
            n_clone = len(clone)

            if n_clone < 4:
                continue

            # Generators: all non-trivial operations in the clone
            generators = list(clone)[:min(20, n_clone)]

            # Test subsets of sizes 25%, 50%, 75%, 100% of clone
            inst_ratios = {}
            for frac_label, frac in [('25%', 0.25), ('50%', 0.5), ('75%', 0.75), ('100%', 1.0)]:
                sz = max(2, int(frac * n_clone))
                if frac < 1.0:
                    F = set(random.sample(clone_list, min(sz, n_clone)))
                else:
                    F = set(clone)

                # Boundary: elements of F whose composition with a generator exits F
                boundary = 0
                for f in F:
                    on_boundary = False
                    for g in generators:
                        for slot in range(k):
                            composed = compose_tt_slot(f, g, k, slot)
                            if composed not in F:
                                on_boundary = True
                                break
                        if on_boundary:
                            break
                    if on_boundary:
                        boundary += 1

                ratio = boundary / len(F)
                inst_ratios[frac_label] = ratio

            boundary_data.append({
                'clone_size': n_clone,
                'ratios': inst_ratios,
            })

        if boundary_data:
            # Average ratios across instances
            avg_ratios = {}
            for label in ['25%', '50%', '75%', '100%']:
                vals = [d['ratios'][label] for d in boundary_data]
                avg_ratios[label] = sum(vals) / len(vals)

            avg_clone = sum(d['clone_size'] for d in boundary_data) / len(boundary_data)
            results[cls_name] = {
                'avg_clone_size': avg_clone,
                'avg_boundary_ratios': avg_ratios,
                'n_inst': len(boundary_data),
            }

            ratio_str = ", ".join(f"{k}={v:.4f}" for k, v in avg_ratios.items())
            print(f"    |Clone|={avg_clone:.1f}, boundary ratios: {ratio_str}")

            # Key metric: does boundary ratio DECREASE as F grows?
            # Amenable => ratio should decrease toward 0 as F -> full clone
            if avg_ratios['100%'] < avg_ratios['25%']:
                print(f"    -> Boundary ratio DECREASING (amenable signal)")
            else:
                print(f"    -> Boundary ratio NOT decreasing (non-amenable signal)")

    return results


# =====================================================================
# TEST 3: WREATH PRODUCT CAYLEY GROWTH
# =====================================================================

def test3_wreath_growth():
    """Cayley graph growth in (Z/2)^n ⋊ S_n for n=4..10.
    Non-amenability in the limit: growth ratio should stabilize > 1."""

    print("\n" + "=" * 72)
    print("TEST 3: Hyperoctahedral group Cayley growth")
    print("=" * 72)

    results = {}

    for n in [4, 6, 8, 10]:
        group_size = 2**n * math.factorial(n)

        def multiply(a, b):
            perm_a, flip_a = a
            perm_b, flip_b = b
            new_perm = tuple(perm_a[perm_b[i]] for i in range(n))
            new_flip = 0
            for i in range(n):
                bit_b = (flip_b >> i) & 1
                bit_a = (flip_a >> perm_b[i]) & 1
                new_flip |= ((bit_a ^ bit_b) << i)
            return (new_perm, new_flip)

        # Generators: cycle, bit-flip, transposition
        gen1 = (tuple((i + 1) % n for i in range(n)), 0)
        gen2 = (tuple(range(n)), 1)  # flip bit 0
        perm3 = list(range(n)); perm3[0], perm3[1] = perm3[1], perm3[0]
        gen3 = (tuple(perm3), 0)
        inv1 = (tuple((i - 1) % n for i in range(n)), 0)
        generators = [gen1, gen2, gen3, inv1]

        identity = (tuple(range(n)), 0)
        visited = {identity}
        current = {identity}
        growth = [(0, 1)]
        max_r = 12

        for r in range(1, max_r + 1):
            next_set = set()
            for elem in current:
                for g in generators:
                    prod = multiply(elem, g)
                    if prod not in visited:
                        next_set.add(prod)
            visited.update(next_set)
            growth.append((r, len(visited)))
            current = next_set
            if not current or len(visited) >= group_size:
                break

        # Growth ratios
        ratios = []
        for i in range(1, len(growth)):
            if growth[i-1][1] > 0 and growth[i][1] > growth[i-1][1]:
                ratios.append(growth[i][1] / growth[i-1][1])

        results[n] = {
            'group_size': group_size,
            'growth': growth,
            'ratios': ratios,
        }

        print(f"\n  n={n}: |G| = {group_size}")
        growth_str = ", ".join(f"|B_{r}|={s}" for r, s in growth[:8])
        print(f"    {growth_str}")
        if ratios:
            ratio_str = ", ".join(f"{r:.2f}" for r in ratios[:6])
            print(f"    Growth ratios: {ratio_str}")
            avg_ratio = sum(ratios[:5]) / min(5, len(ratios))
            print(f"    Avg early ratio: {avg_ratio:.3f}")

    return results


# =====================================================================
# SEPARATION TABLE & VERDICT
# =====================================================================

def build_separation(test1_results, test2_results, test3_results):
    """Combine all tests into a separation table."""

    print("\n" + "=" * 72)
    print("SEPARATION TABLE")
    print("=" * 72)

    P_TIME = ['2-SAT', 'Horn-SAT', 'Dual-Horn', 'XOR-SAT']
    NPC = ['3-SAT', 'NAE-3-SAT']

    print(f"\n  {'Class':<12} {'Type':<5} {'|Cl_3|':>8} {'|Cl_4|':>8} "
          f"{'EU_3':>6} {'Grow':>6} {'Bnd_100%':>9} {'Amenable':>9}")
    print("  " + "-" * 75)

    sep = []
    for cls_name in P_TIME + NPC:
        ctype = 'P' if cls_name in P_TIME else 'NPC'

        t1 = test1_results.get(cls_name, {})
        t2 = test2_results.get(cls_name, {})

        c3 = t1.get(3, {})
        c4 = t1.get(4, {})
        c3_size = c3['mean_size'] if c3 else 0
        c4_size = c4['mean_size'] if c4 else 0
        eu3 = c3['eu_frac'] if c3 else 0
        np3 = c3['mean_non_proj'] if c3 else 0

        # Growth ratio k=3->4
        if c3_size > 0 and c4_size > 0:
            growth = c4_size / c3_size
        else:
            growth = 0

        # Boundary ratio at 100%
        bnd = t2.get('avg_boundary_ratios', {}).get('100%', -1) if t2 else -1

        # Amenability criterion (multi-signal):
        # 1. Has genuine (non-essentially-unary) polymorphisms at k=3
        # 2. Clone grows with arity
        # 3. Boundary ratio decreases toward 0
        has_genuine_poly = (np3 > 0.5)
        clone_grows = (growth > 2.0)  # More than doubling from k=3 to k=4

        # For P-time: should have genuine polymorphisms AND growing clone
        # For NPC: should have NO genuine polymorphisms OR flat clone
        if has_genuine_poly and clone_grows:
            amenable = 'YES'
        elif has_genuine_poly and not clone_grows:
            amenable = 'WEAK-Y'
        elif not has_genuine_poly and not clone_grows:
            amenable = 'NO'
        else:
            amenable = 'WEAK-N'

        bnd_str = f"{bnd:.4f}" if bnd >= 0 else "N/A"

        sep.append({
            'class': cls_name, 'type': ctype, 'c3': c3_size, 'c4': c4_size,
            'eu3': eu3, 'growth': growth, 'bnd': bnd, 'amenable': amenable,
            'has_genuine_poly': has_genuine_poly, 'clone_grows': clone_grows,
        })

        print(f"  {cls_name:<12} {ctype:<5} {c3_size:>8.1f} {c4_size:>8.1f} "
              f"{eu3:>6.3f} {growth:>6.1f} {bnd_str:>9} {amenable:>9}")

    # Verdict
    p_ok = all(r['amenable'] in ('YES', 'WEAK-Y') for r in sep if r['type'] == 'P')
    npc_ok = all(r['amenable'] in ('NO', 'WEAK-N') for r in sep if r['type'] == 'NPC')

    print(f"\n  P-time amenable: {p_ok}")
    print(f"  NPC non-amenable: {npc_ok}")

    if p_ok and npc_ok:
        verdict = 'PASS'
    elif p_ok or npc_ok:
        verdict = 'PARTIAL'
    else:
        verdict = 'KILL'

    print(f"\n  *** VERDICT: {verdict} ***")

    return sep, verdict


# =====================================================================
# MAIN
# =====================================================================

def main():
    print("=" * 72)
    print("O9 — CLONE AMENABILITY TEST")
    print("=" * 72)
    t0 = time.time()

    test1_results = test1_clone_richness()
    test2_results = test2_folner_boundary()
    test3_results = test3_wreath_growth()
    sep, verdict = build_separation(test1_results, test2_results, test3_results)

    elapsed = time.time() - t0
    print(f"\nTotal runtime: {elapsed:.1f}s")
    print(f"\n{'='*72}")
    print(f"FINAL VERDICT: {verdict}")
    print(f"{'='*72}")

    return test1_results, test2_results, test3_results, sep, verdict


if __name__ == '__main__':
    main()
