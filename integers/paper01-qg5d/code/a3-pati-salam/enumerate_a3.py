#!/usr/bin/env python3
"""
A_3 root-lattice theta series and invariant analysis.

Hypothesis (Paper 1, PROOF-CHAIN.md section E.3, Lead #1):
  alpha_PS^-1 = 17 (Pin #9) is a counting invariant of the A_3 = D_3 = SU(4)
  root-lattice quadratic form

    Q_3(n) = n_1^2 + n_2^2 + n_3^2 + n_1 n_2 + n_1 n_3 + n_2 n_3

  appearing in the 3-loop Mercedes KK-mass sum (Route-C, paper1/code/K-5-2-route-c-3loop.py).

This script:
  1. Enumerates short vectors of A_3 in the Z^3 / Q_3 realization up to Q_3(v) = N_MAX.
  2. Tabulates theta-series coefficients r_{Q_3}(n) = #{v in Z^3 : Q_3(v) = n}.
  3. Computes partial sums and checks for 17 as a natural invariant.
  4. Tests combinations with the Route-C residue 2*sqrt(2*pi).
  5. Writes JSON + informs the FINDINGS.md report.

Usage:
  /Users/gsix/quantum-geometry-in-5d-latex/paper1/code/zeta-zeros/venv/bin/python enumerate_a3.py
"""

import json
import math
import os
from collections import Counter, defaultdict
from fractions import Fraction

N_MAX = 60  # enumerate Q_3(v) up to this; theta reported through n=30
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def Q3(n1, n2, n3):
    """A_3 positive-definite quadratic form (Cartan form of SU(4))."""
    return n1 * n1 + n2 * n2 + n3 * n3 + n1 * n2 + n1 * n3 + n2 * n3


def enumerate_theta(n_max):
    """Enumerate all v in Z^3 with Q_3(v) <= n_max.

    Q_3 is positive-definite with minimum eigenvalue (1 - 1/sqrt(3))/... > 0;
    a safe box is |n_i| <= ceil(sqrt(2*n_max)) since Q_3(v) >= |v|^2 / 2 for
    the Gram matrix with diagonal 1 and off-diagonal 1/2 (eigenvalues 1/2, 1/2, 2).
    """
    bound = int(math.ceil(math.sqrt(2 * n_max))) + 2
    counts = Counter()
    vectors_by_norm = defaultdict(list)
    for n1 in range(-bound, bound + 1):
        for n2 in range(-bound, bound + 1):
            for n3 in range(-bound, bound + 1):
                q = Q3(n1, n2, n3)
                if 0 <= q <= n_max:
                    counts[q] += 1
                    if q <= 10:  # only store small-norm vectors
                        vectors_by_norm[q].append((n1, n2, n3))
    return counts, vectors_by_norm


def partial_sums(theta, n_max):
    s = 0
    out = []
    for n in range(n_max + 1):
        s += theta.get(n, 0)
        out.append(s)
    return out


def find_17(theta, partials, n_max):
    """Hunt for 17 in a dozen natural ways."""
    hits = []

    # (a) r_{Q_3}(n) == 17 for some n
    for n in range(n_max + 1):
        if theta.get(n, 0) == 17:
            hits.append({"mechanism": f"r_Q3({n}) = 17", "n": n, "value": 17})

    # (b) partial sum == 17
    for n, s in enumerate(partials):
        if s == 17:
            hits.append({"mechanism": f"sum_{{k=0..{n}}} r_Q3(k) = 17", "n": n, "value": s})

    # (c) excluding zero vector: 1 + partial
    for n in range(n_max + 1):
        s = partials[n] - 1  # drop v=0
        if s == 17:
            hits.append({"mechanism": f"nonzero vectors with Q_3 <= {n} = 17", "n": n, "value": s})

    # (d) difference of successive shells
    for n in range(1, n_max + 1):
        d = theta.get(n, 0) - theta.get(n - 1, 0)
        if d == 17:
            hits.append({"mechanism": f"r_Q3({n}) - r_Q3({n-1}) = 17", "n": n, "value": d})

    # (e) r_Q3(n) + 1 (closing with zero vector)
    for n in range(1, n_max + 1):
        if theta.get(n, 0) + 1 == 17:
            hits.append({"mechanism": f"r_Q3({n}) + 1 = 17", "n": n, "value": 17})

    # (f) r_Q3(n) for the norm-n shell as orbit count: |v|^2 / 2 etc.
    # Already covered above.

    return hits


def test_residue_combinations():
    """2*sqrt(2*pi) ~ 8.885765876...; check if 17 is reachable via short combos."""
    R = 2.0 * math.sqrt(2.0 * math.pi)
    probes = {
        "2*sqrt(2pi)": R,
        "2*sqrt(2pi) * 2": 2 * R,
        "2*sqrt(2pi) * sqrt(pi)": R * math.sqrt(math.pi),
        "4*pi": 4 * math.pi,
        "17 / (2*sqrt(2pi))": 17 / R,
        "17 / (2*sqrt(2pi))^2": 17 / (R * R),
        "ln(17) / ln(2*sqrt(2pi))": math.log(17) / math.log(R),
    }
    # Look for near-integer / near-rational values
    out = {}
    for name, val in probes.items():
        nearest_int = round(val)
        err = abs(val - nearest_int)
        out[name] = {"value": val, "nearest_int": nearest_int, "err": err, "integer_match": err < 1e-6}
    return out


def pati_salam_dimensions():
    """Pati-Salam group dimension counting.

    Pati-Salam = SU(4) x SU(2)_L x SU(2)_R
      dim SU(4) = 15
      dim SU(2) = 3 each
      total Lie algebra dim = 15 + 3 + 3 = 21 (too big)

    But the statement in the hypothesis is:
      "SU(4) has 15 generators; plus two U(1) factors giving 15+1+1 = 17 if relevant".

    Let's enumerate natural combinations that land on 17.
    """
    combos = {
        "dim SU(4)": 15,
        "dim SU(4) + 2*U(1) = 15 + 1 + 1": 17,
        "dim SU(4) + rank SU(4) = 15 + 3": 18,
        "dim SU(4) + rank A_3 - 1 = 15 + 2": 17,  # rank(A_3)=3, minus CoM? same as above
        "|positive roots A_3| + rank A_3 = 6 + 3": 9,
        "|roots A_3| + rank A_3 = 12 + 3": 15,
        "|roots A_3| + |short roots| = 12 + ?": None,
        "|roots A_3| + dim Cartan + 2 = 12 + 3 + 2": 17,
        "|roots A_3 (12)| + 1 (zero) + rank (3) + 1 = 17": 17,
        "dim SU(4) (15) + Z/4 order / 2 = 15 + 2": 17,
        "r_Q3(1) = 12 (root vectors) + 5 ?": None,
    }
    return combos


def a3_invariants():
    """Common A_3 invariants for reference."""
    return {
        "rank": 3,
        "dim_lie_algebra": 15,  # SU(4) = A_3
        "num_positive_roots": 6,
        "num_roots_total": 12,
        "coxeter_number_h": 4,
        "dual_coxeter_number": 4,
        "discriminant": 4,  # det of Cartan matrix of A_3
        "weyl_group_order": 24,  # |S_4|
        "fundamental_group_order": 4,  # Z/4 for A_3 (center of SU(4))
        "num_minuscule_reps": 2,  # fundamental reps 4, 6, bar{4}; minuscule: 4 and bar{4}
        "minimal_vectors_count": 12,  # |Delta| = 12 (the short vectors at norm 1 in Q_3)
        "kissing_number_A3": 12,
    }


def main():
    print(f"Enumerating A_3 theta series up to Q_3 = {N_MAX}...")
    theta, vectors = enumerate_theta(N_MAX)
    partials = partial_sums(theta, N_MAX)

    print("\nTheta series r_{Q_3}(n) for n=0..30:")
    print(f"{'n':>3} | {'r_Q3(n)':>8} | {'sum_{k<=n}':>10}")
    print("-" * 32)
    for n in range(31):
        print(f"{n:>3} | {theta.get(n,0):>8} | {partials[n]:>10}")

    hits = find_17(theta, partials, N_MAX)
    print("\nOccurrences of 17:")
    if not hits:
        print("  (none found)")
    for h in hits:
        print(f"  {h['mechanism']}")

    residues = test_residue_combinations()
    print("\nResidue / constant combinations (2*sqrt(2*pi) = {:.10f}):".format(2.0 * math.sqrt(2.0 * math.pi)))
    for name, d in residues.items():
        tag = " *** INTEGER" if d["integer_match"] else ""
        print(f"  {name:40s} = {d['value']:.10f}  (nearest int {d['nearest_int']}, err {d['err']:.3e}){tag}")

    ps = pati_salam_dimensions()
    inv = a3_invariants()
    print("\nPati-Salam / A_3 dimension combinations landing on 17:")
    for name, v in ps.items():
        mark = "  <- HIT" if v == 17 else ""
        print(f"  {name:55s} = {v}{mark}")

    # Small-norm vector listings
    print("\nShort vectors by norm (Q_3 <= 4):")
    for n in range(5):
        vs = vectors.get(n, [])
        print(f"  Q_3 = {n}: {len(vs)} vectors")
        if 0 < n <= 2:
            for v in vs[:20]:
                print(f"    {v}")

    # Build output JSON
    out = {
        "form": "Q_3(n) = n1^2 + n2^2 + n3^2 + n1*n2 + n1*n3 + n2*n3",
        "description": "Theta series of A_3 = D_3 = SU(4) root lattice in its Z^3 realization",
        "n_max_enumerated": N_MAX,
        "theta_coefficients": {str(n): theta.get(n, 0) for n in range(N_MAX + 1)},
        "partial_sums_inclusive": {str(n): partials[n] for n in range(N_MAX + 1)},
        "partial_sums_excluding_zero": {str(n): partials[n] - 1 for n in range(N_MAX + 1)},
        "occurrences_of_17": hits,
        "residue_combinations": residues,
        "pati_salam_dim_combos": ps,
        "a3_invariants": inv,
        "short_vectors_by_norm": {
            str(n): {"count": len(vectors.get(n, [])), "examples": vectors.get(n, [])[:24]}
            for n in range(5)
        },
    }
    json_path = os.path.join(OUT_DIR, "a3_theta_series.json")
    with open(json_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {json_path}")

    return out


if __name__ == "__main__":
    main()
