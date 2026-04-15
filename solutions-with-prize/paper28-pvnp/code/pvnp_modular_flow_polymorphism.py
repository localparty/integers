"""
pvnp_modular_flow_polymorphism.py — Does the modular flow produce
the polymorphism?

The key experiment for Strategy 02 (P → Taylor via modular flow).
For each P-time Schaefer class, we test whether the BC modular
flow's action on the solution space produces the known Taylor
polymorphism.

Three alternative mechanisms tested:
(A) Direct modular flow: σ_t acts by phases on solution operators.
    Do the phases encode the polymorphism?
(B) Conditional expectation: E_{P-sector} projects NP operators
    onto the P sector. Does the projection produce the polymorphism?
(C) Commutant: the fixed-point algebra of σ_t on the solution space.
    Is the polymorphism the generating operation of this algebra?

Author: G Six, with Claude Opus 4.6. Date: 2026-04-11.
"""

import random
import itertools
import math
import numpy as np

random.seed(42)
np.set_printoptions(precision=6, suppress=True)

# =====================================================================
# UTILITY: solution finding and polymorphism checking
# =====================================================================

def find_solutions(clauses, n, mode='or'):
    solutions = []
    for bits in itertools.product([0, 1], repeat=n):
        sat = True
        for clause in clauses:
            if mode == 'or':
                ok = any((lit > 0 and bits[abs(lit)-1] == 1) or
                         (lit < 0 and bits[abs(lit)-1] == 0) for lit in clause)
                if not ok: sat = False; break
            elif mode == 'xor':
                count = sum(1 for lit in clause
                           if (lit > 0 and bits[abs(lit)-1] == 1) or
                              (lit < 0 and bits[abs(lit)-1] == 0))
                if count % 2 == 0: sat = False; break
        if sat:
            solutions.append(bits)
    return solutions

def median3(a, b, c):
    return tuple(1 if (a[i]+b[i]+c[i]) >= 2 else 0 for i in range(len(a)))

def xor3(a, b, c):
    return tuple((a[i]+b[i]+c[i]) % 2 for i in range(len(a)))

def and2(a, b):
    return tuple(a[i] & b[i] for i in range(len(a)))

def or2(a, b):
    return tuple(a[i] | b[i] for i in range(len(a)))


# =====================================================================
# THE BC MODULAR FLOW ON SOLUTION SPACES
# =====================================================================

def bc_modular_phase(solution, t):
    """Compute the BC modular flow phase for a solution.
    In the BC system, σ_t(μ_n) = n^{it} μ_n. For a solution
    encoded as a bit string b ∈ {0,1}^n, the corresponding
    "number" is n(b) = Σ_i b_i * 2^i + 1 (binary encoding + 1
    to avoid n=0). The phase is n(b)^{it}."""
    n_val = sum(b * (2**i) for i, b in enumerate(solution)) + 1
    return np.exp(1j * t * np.log(n_val))

def bc_modular_weight(solution, beta=1.0):
    """KMS weight of a solution at inverse temperature beta.
    w(b) = n(b)^{-beta}."""
    n_val = sum(b * (2**i) for i, b in enumerate(solution)) + 1
    return n_val ** (-beta)


# =====================================================================
# TEST A: Phase-pattern analysis
# =====================================================================

print("=" * 70)
print("TEST A: BC modular flow phase patterns on solution spaces")
print("=" * 70)

def analyze_phase_pattern(solutions, t_values, name):
    """For each t, compute the phase of each solution and analyze
    whether the phase pattern encodes a polymorphism."""
    n_sols = len(solutions)
    if n_sols < 3:
        print(f"  {name}: too few solutions ({n_sols})")
        return

    phases = {}
    for t in t_values:
        phases[t] = [bc_modular_phase(s, t) for s in solutions]

    print(f"\n  {name}: {n_sols} solutions")
    print(f"  Phase pattern at t=1.0:")
    for i, s in enumerate(solutions[:8]):
        p = phases[1.0][i]
        print(f"    sol {i}: {''.join(str(b) for b in s)}  "
              f"phase = {p.real:+.4f} {p.imag:+.4f}i  "
              f"|phase| = {abs(p):.6f}")

    # Check: does the phase ordering match the polymorphism structure?
    # For median: solutions that are "medians" of others should have
    # intermediate phases.
    if n_sols >= 3:
        print(f"\n  Median test: for triples (a,b,c), does median(a,b,c)'s")
        print(f"  phase lie between the phases of a, b, c?")
        sol_set = set(solutions)
        n_tested = 0
        n_intermediate = 0
        for i in range(min(n_sols, 10)):
            for j in range(i+1, min(n_sols, 10)):
                for k in range(j+1, min(n_sols, 10)):
                    med = median3(solutions[i], solutions[j], solutions[k])
                    if med in sol_set:
                        med_idx = solutions.index(med)
                        pa = phases[1.0][i].real
                        pb = phases[1.0][j].real
                        pc = phases[1.0][k].real
                        pm = phases[1.0][med_idx].real
                        lo = min(pa, pb, pc)
                        hi = max(pa, pb, pc)
                        n_tested += 1
                        if lo <= pm <= hi:
                            n_intermediate += 1
        if n_tested > 0:
            print(f"    {n_intermediate}/{n_tested} medians have intermediate "
                  f"phase ({100*n_intermediate/n_tested:.1f}%)")

# Test on 2-SAT
n = 8
clauses_2sat = [[v if random.random() < 0.5 else -v
                  for v in random.sample(range(1, n+1), 2)]
                 for _ in range(int(1.5*n))]
sols_2sat = find_solutions(clauses_2sat, n)
analyze_phase_pattern(sols_2sat, [0.5, 1.0, 2.0, 5.0], "2-SAT")

# Test on XOR-SAT
clauses_xor = [[v if random.random() < 0.5 else -v
                 for v in random.sample(range(1, n+1), 3)]
                for _ in range(int(0.5*n))]
sols_xor = find_solutions(clauses_xor, n, mode='xor')
analyze_phase_pattern(sols_xor, [0.5, 1.0, 2.0, 5.0], "XOR-SAT")


# =====================================================================
# TEST B: Conditional expectation onto the P-time sector
# =====================================================================

print("\n" + "=" * 70)
print("TEST B: Conditional expectation — projecting onto P-sector")
print("=" * 70)

def conditional_expectation_test(solutions, polymorphism, poly_name, arity=3):
    """Test whether the KMS-weighted average over the solution space
    (the conditional expectation) produces the polymorphism.

    For each pair/triple of solutions, compute:
    (a) The polymorphism output: f(x,y,z)
    (b) The KMS-weighted average: Σ_s w(s) * s / Σ w(s), evaluated
        at the polymorphism inputs
    (c) Whether they agree
    """
    sol_set = set(solutions)
    n_sols = len(solutions)
    if n_sols < arity:
        return

    # KMS weights at beta=1
    weights = {s: bc_modular_weight(s, beta=1.0) for s in solutions}
    total_w = sum(weights.values())

    # The "KMS center of mass" of the solution space
    n_bits = len(solutions[0])
    center = np.zeros(n_bits)
    for s in solutions:
        center += np.array(s) * weights[s]
    center /= total_w

    print(f"\n  KMS center of mass of {poly_name} solution space:")
    print(f"    center = [{', '.join(f'{c:.4f}' for c in center)}]")
    print(f"    (round to {tuple(1 if c > 0.5 else 0 for c in center)})")

    # Test: for each triple of solutions, compute:
    # (a) polymorphism output
    # (b) KMS-weighted interpolation
    n_tested = 0
    n_agree = 0
    for _ in range(min(500, n_sols**arity)):
        if arity == 3:
            idx = random.sample(range(n_sols), 3)
            poly_out = polymorphism(solutions[idx[0]], solutions[idx[1]], solutions[idx[2]])
        else:
            idx = random.sample(range(n_sols), 2)
            poly_out = polymorphism(solutions[idx[0]], solutions[idx[1]])

        if poly_out not in sol_set:
            continue

        # KMS-weighted interpolation: for each bit position, take
        # the weighted vote
        inputs = [solutions[i] for i in idx]
        kms_interp = []
        for bit in range(n_bits):
            weighted_vote = sum(inputs[j][bit] * weights[inputs[j]]
                              for j in range(len(inputs)))
            total_input_w = sum(weights[inputs[j]] for j in range(len(inputs)))
            kms_interp.append(1 if weighted_vote / total_input_w > 0.5 else 0)
        kms_interp = tuple(kms_interp)

        n_tested += 1
        if kms_interp == poly_out:
            n_agree += 1

    if n_tested > 0:
        print(f"    KMS-weighted interpolation agrees with {poly_name}: "
              f"{n_agree}/{n_tested} ({100*n_agree/n_tested:.1f}%)")
    else:
        print(f"    No valid triples to test")

# 2-SAT: does KMS-weighted interpolation = median?
print("\n  2-SAT:")
if len(sols_2sat) >= 3:
    conditional_expectation_test(sols_2sat, median3, "median", arity=3)

# XOR-SAT: does KMS-weighted interpolation = XOR?
print("\n  XOR-SAT:")
if len(sols_xor) >= 3:
    conditional_expectation_test(sols_xor, xor3, "XOR", arity=3)

# Fresh Horn-SAT
clauses_horn = []
for _ in range(int(2.0*n)):
    k = random.randint(2, 3)
    vs = random.sample(range(1, n+1), min(k, n))
    pos = random.randint(0, len(vs))
    clause = [-v if i != pos else v for i, v in enumerate(vs)]
    clauses_horn.append(clause)
sols_horn = find_solutions(clauses_horn, n)
print("\n  Horn-SAT:")
if len(sols_horn) >= 2:
    conditional_expectation_test(sols_horn, and2, "AND", arity=2)


# =====================================================================
# TEST C: The commutant / fixed-point structure
# =====================================================================

print("\n" + "=" * 70)
print("TEST C: Fixed-point algebra of σ_t on solution spaces")
print("=" * 70)

def fixed_point_analysis(solutions, name):
    """Analyze the fixed-point structure of σ_t on the solution space.
    Two solutions s, s' are "σ_t-equivalent" if they acquire the
    same phase under σ_t for ALL t. This happens iff n(s) = n(s'),
    i.e., they have the same binary encoding."""
    if len(solutions) < 2:
        print(f"\n  {name}: too few solutions")
        return

    # Group solutions by their "n-value" (binary encoding)
    n_vals = {}
    for s in solutions:
        nv = sum(b * (2**i) for i, b in enumerate(s)) + 1
        if nv not in n_vals:
            n_vals[nv] = []
        n_vals[nv].append(s)

    # Each n-value class is a "fixed-point orbit" of σ_t
    n_classes = len(n_vals)
    n_singleton = sum(1 for v in n_vals.values() if len(v) == 1)
    n_multi = sum(1 for v in n_vals.values() if len(v) > 1)

    print(f"\n  {name}: {len(solutions)} solutions, {n_classes} phase classes")
    print(f"    Singletons: {n_singleton}, Multi-solution classes: {n_multi}")

    if n_multi > 0:
        print(f"    Multi-solution classes (solutions with same n-value):")
        for nv, sols in sorted(n_vals.items()):
            if len(sols) > 1:
                print(f"      n={nv}: {len(sols)} solutions: "
                      f"{[''.join(str(b) for b in s) for s in sols[:3]]}")

    # The fixed-point algebra is generated by operators that
    # are constant on each phase class. The polymorphism should
    # be the simplest operation that respects the class structure.

    # Test: for each pair of solutions in the same class, is one
    # reachable from the other by the known polymorphism?
    sol_set = set(solutions)
    n_reachable = 0
    n_pairs = 0
    for nv, sols in n_vals.items():
        if len(sols) > 1:
            for i in range(len(sols)):
                for j in range(i+1, len(sols)):
                    n_pairs += 1
                    # Check if median of (s_i, s_j, any third solution) = s_i or s_j
                    for k, s3 in enumerate(solutions):
                        med = median3(sols[i], sols[j], s3)
                        if med == sols[i] or med == sols[j]:
                            n_reachable += 1
                            break

    if n_pairs > 0:
        print(f"    Same-class pairs reachable by median: "
              f"{n_reachable}/{n_pairs} ({100*n_reachable/n_pairs:.1f}%)")

fixed_point_analysis(sols_2sat, "2-SAT")
fixed_point_analysis(sols_xor, "XOR-SAT")
fixed_point_analysis(sols_horn, "Horn-SAT")


# =====================================================================
# TEST D: KMS weighting as majority vote
# =====================================================================

print("\n" + "=" * 70)
print("TEST D: Does KMS weighting reproduce the polymorphism directly?")
print("=" * 70)

def kms_polymorphism_test(solutions, known_poly, poly_name, arity=3):
    """For each k-tuple of solutions, compare:
    (a) Known polymorphism applied directly
    (b) KMS-weighted bit-majority vote
    (c) Uniform-weighted bit-majority vote (= standard median)

    If (a) == (b) ≠ (c), the KMS weights are doing something
    non-trivial that reproduces the polymorphism.
    If (a) == (c), the polymorphism IS the uniform majority
    (= standard median), and KMS weights don't matter.
    """
    sol_set = set(solutions)
    n_sols = len(solutions)
    n_bits = len(solutions[0])
    if n_sols < arity:
        return

    weights = {s: bc_modular_weight(s, beta=1.0) for s in solutions}

    n_tested = 0
    n_agree_kms = 0
    n_agree_uniform = 0
    n_kms_neq_uniform = 0

    for _ in range(min(1000, n_sols**arity)):
        idx = random.sample(range(n_sols), arity)
        inputs = [solutions[i] for i in idx]

        # (a) Known polymorphism
        if arity == 3:
            poly_out = known_poly(inputs[0], inputs[1], inputs[2])
        else:
            poly_out = known_poly(inputs[0], inputs[1])

        if poly_out not in sol_set:
            continue

        # (b) KMS-weighted majority
        kms_result = []
        for bit in range(n_bits):
            w1 = sum(inputs[j][bit] * weights[inputs[j]] for j in range(arity))
            w0 = sum((1-inputs[j][bit]) * weights[inputs[j]] for j in range(arity))
            kms_result.append(1 if w1 > w0 else 0)
        kms_result = tuple(kms_result)

        # (c) Uniform majority
        uniform_result = []
        for bit in range(n_bits):
            ones = sum(inputs[j][bit] for j in range(arity))
            uniform_result.append(1 if ones > arity/2 else 0)
        uniform_result = tuple(uniform_result)

        n_tested += 1
        if kms_result == poly_out:
            n_agree_kms += 1
        if uniform_result == poly_out:
            n_agree_uniform += 1
        if kms_result != uniform_result:
            n_kms_neq_uniform += 1

    if n_tested > 0:
        print(f"\n  {poly_name} ({n_tested} valid tuples):")
        print(f"    Known poly == KMS-weighted majority: "
              f"{n_agree_kms}/{n_tested} ({100*n_agree_kms/n_tested:.1f}%)")
        print(f"    Known poly == uniform majority:      "
              f"{n_agree_uniform}/{n_tested} ({100*n_agree_uniform/n_tested:.1f}%)")
        print(f"    KMS ≠ uniform:                       "
              f"{n_kms_neq_uniform}/{n_tested} ({100*n_kms_neq_uniform/n_tested:.1f}%)")

# Run on multiple fresh instances for each class
print("\n  Running on multiple fresh instances...")

for csp_name, k, alpha, mode, poly, poly_name, arity in [
    ("2-SAT", 2, 1.5, 'or', median3, "median", 3),
    ("XOR-SAT", 3, 0.5, 'xor', xor3, "XOR", 3),
]:
    print(f"\n  === {csp_name} ===")
    total_kms = total_unif = total_tested = total_diff = 0
    n_instances = 0
    for trial in range(30):
        n = 8
        clauses = [[v if random.random() < 0.5 else -v
                     for v in random.sample(range(1, n+1), k)]
                    for _ in range(int(alpha*n))]
        sols = find_solutions(clauses, n, mode=mode)
        if len(sols) < arity:
            continue
        n_instances += 1
        sol_set = set(sols)
        weights = {s: bc_modular_weight(s, beta=1.0) for s in sols}
        n_bits = len(sols[0])

        for _ in range(min(200, len(sols)**arity)):
            idx = random.sample(range(len(sols)), arity)
            inputs = [sols[i] for i in idx]
            if arity == 3:
                po = poly(inputs[0], inputs[1], inputs[2])
            else:
                po = poly(inputs[0], inputs[1])
            if po not in sol_set:
                continue
            total_tested += 1

            kms_r = tuple(1 if sum(inputs[j][b]*weights[inputs[j]]
                         for j in range(arity)) >
                         sum((1-inputs[j][b])*weights[inputs[j]]
                         for j in range(arity)) else 0
                         for b in range(n_bits))
            unif_r = tuple(1 if sum(inputs[j][b] for j in range(arity))
                          > arity/2 else 0 for b in range(n_bits))

            if kms_r == po: total_kms += 1
            if unif_r == po: total_unif += 1
            if kms_r != unif_r: total_diff += 1

    if total_tested > 0:
        print(f"    {n_instances} instances, {total_tested} valid tuples")
        print(f"    Known poly == KMS majority:     "
              f"{total_kms}/{total_tested} ({100*total_kms/total_tested:.1f}%)")
        print(f"    Known poly == uniform majority:  "
              f"{total_unif}/{total_tested} ({100*total_unif/total_tested:.1f}%)")
        print(f"    KMS ≠ uniform:                   "
              f"{total_diff}/{total_tested} ({100*total_diff/total_tested:.1f}%)")


# =====================================================================
# SUMMARY
# =====================================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
EXPERIMENT RESULTS:

TEST A (Phase patterns): The BC modular flow assigns phases to
  solutions via n(b)^{it}. Solutions with similar binary encodings
  get similar phases. The phase pattern structures the solution
  space but does not directly permute solutions.

TEST B (Conditional expectation): KMS-weighted interpolation of
  solution tuples. Tests whether the KMS-weight-weighted majority
  vote reproduces the known polymorphism.

TEST C (Fixed-point algebra): Solutions with the same binary
  encoding form "phase equivalence classes." The polymorphism
  should respect these classes.

TEST D (KMS vs uniform majority): The critical question — does
  KMS weighting (the BC modular flow's contribution) make a
  difference compared to uniform weighting?

  If KMS majority == known polymorphism and KMS ≠ uniform:
    → The modular flow DOES produce the polymorphism, and it's
      different from naive majority. This supports the theorem.

  If uniform majority == known polymorphism:
    → The polymorphism is just majority voting (median), and the
      KMS weights don't contribute. The theorem needs revision.

  If neither matches well:
    → The polymorphism arises from a different mechanism than
      weighted majority. Explore alternatives.
""")
