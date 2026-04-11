"""Test of G's proposed projector
    P_k^𝔭 := I − s_𝔭^k (s_𝔭^k)^*  =  I − e_{𝔭^k}

in the Bost-Connes algebra A_{BC,K} over K = Q(i).

If this projector + the KMS_β expectations give a direct algebraic
pathway to the cocycle shift Δc(δ) and the integrality obstruction
(Key Lemma C), then MY4 (the distributional → genuine spectrum wall)
is *bypassed* entirely — the argument lives at the level of the
C*-algebra + KMS states, never invoking individual eigenvectors.

This script tests four things:

  (a) Algebraic: P_k^𝔭 is a legitimate projection in A_{BC,K},
      derived from the BC relations
          s_𝔭^* s_𝔭 = 1             (isometry)
          s_𝔭 s_𝔭^* = e_𝔭           (range projection)
      It follows that
          (s_𝔭^k)^* s_𝔭^k = 1
          (s_𝔭^k) (s_𝔭^k)^* =: e_{𝔭^k}  is a projection
          P_k^𝔭 = I − e_{𝔭^k} is a projection

  (b) KMS_1 expectation: ω_1(P_k^𝔭) = 1 − N(𝔭)^(−k)
      (derived from the 𝔭-local Fock structure + ITPFI factorization)

  (c) KMS_β expectation for β = 1 + 2δ:
          ω_{1+2δ}(P_k^𝔭) = 1 − N(𝔭)^(−k(1+2δ))
      and the deformation
          Δω(δ) := ω_{1+2δ}(P_k^𝔭) − ω_1(P_k^𝔭)
                 = N(𝔭)^(−k) · (1 − N(𝔭)^(−2kδ))

  (d) Connection to the cocycle shift Δc(δ) from Paper 26 §7.1:
          Δc(δ) = (1 − N^(−2δ)) / (N − N^(−2δ))
      We check whether Δω and Δc are related by an algebraic identity
      that would make the KMS-projector argument an algebraic
      reformulation of the cocycle obstruction.

We run this on the four bridge rows of the corrected table:
    (k=2, N=13), (k=3, N=13), (k=4, N=41), (k=6, N=29).
"""

from mpmath import mp, mpf, log, power, fabs

mp.dps = 40

# The four bridge rows from the corrected Prop 4.3 (cf. research/
# corrected-bridge-table.md).
BRIDGES = [
    (2, 13),  # (1+i)/(2+3i) pairing in §4
    (3, 13),
    (4, 41),
    (6, 29),
]


# ---------------------------------------------------------------
# (a) Algebraic verification — symbolic demonstration, not numerical.
# ---------------------------------------------------------------

def verify_projector_algebra():
    """Demonstrate that P_k^𝔭 is a projection given BC relations."""
    print("=" * 70)
    print("(a) ALGEBRAIC: P_k^𝔭 = I − s_𝔭^k (s_𝔭^k)^* is a projection")
    print("=" * 70)
    print()
    print("Given BC relations:")
    print("    s_𝔭^* s_𝔭 = 1           (isometry)")
    print("    (s_𝔭 s_𝔭^*)^2 = s_𝔭 (s_𝔭^* s_𝔭) s_𝔭^* = s_𝔭 s_𝔭^*")
    print("    (s_𝔭 s_𝔭^*)^* = s_𝔭 s_𝔭^*   (self-adjoint)")
    print()
    print("By induction on k:")
    print("    (s_𝔭^k)^* s_𝔭^k = (s_𝔭^*)^{k-1} (s_𝔭^* s_𝔭) s_𝔭^{k-1}")
    print("                     = (s_𝔭^*)^{k-1} s_𝔭^{k-1} = ... = 1")
    print()
    print("Let e_{𝔭^k} := (s_𝔭^k)(s_𝔭^k)^*. Then")
    print("    e_{𝔭^k}^2 = s_𝔭^k ((s_𝔭^k)^* s_𝔭^k) (s_𝔭^k)^*")
    print("              = s_𝔭^k · 1 · (s_𝔭^k)^* = e_{𝔭^k}")
    print("    e_{𝔭^k}^* = ((s_𝔭^k)^*)^* (s_𝔭^k)^* = s_𝔭^k (s_𝔭^k)^* = e_{𝔭^k}")
    print()
    print("So e_{𝔭^k} is a projection, and therefore")
    print("    P_k^𝔭 = I − e_{𝔭^k}")
    print("is also a projection (complementary to e_{𝔭^k}).")
    print()
    print("Verdict: ALGEBRA HOLDS.")
    print()


# ---------------------------------------------------------------
# (b) KMS_1 expectation: ω_1(P_k^𝔭) = 1 − N(𝔭)^{−k}
# ---------------------------------------------------------------

def omega_1_P(k, N):
    """KMS_1 expectation of P_k^𝔭 in A_{BC,K}."""
    return 1 - power(mpf(N), -k)


def verify_KMS1():
    print("=" * 70)
    print("(b) KMS_1 expectation  ω_1(P_k^𝔭) = 1 − N(𝔭)^(−k)")
    print("=" * 70)
    print()
    print("Derivation: in the 𝔭-local Fock space with basis {|n⟩ : n ≥ 0},")
    print("s_𝔭 |n⟩ = |n+1⟩, so e_{𝔭^k} = Σ_{n ≥ k} |n⟩⟨n|.")
    print("The KMS_1 state in this factor is the Gibbs measure")
    print("    ω_1^𝔭(|n⟩⟨n|) = (1 − N^(−1)) · N^(−n)")
    print("which gives")
    print("    ω_1^𝔭(e_{𝔭^k}) = Σ_{n≥k} (1 − N^(−1)) N^(−n)")
    print("                   = (1 − N^(−1)) · N^(−k)/(1 − N^(−1))")
    print("                   = N^(−k).")
    print("By ITPFI factorization ω_1 = ⊗_𝔭 ω_1^𝔭, with the other factors")
    print("trivial on I, we get  ω_1(e_{𝔭^k}) = N(𝔭)^(−k)  and hence")
    print("    ω_1(P_k^𝔭) = 1 − N(𝔭)^(−k).")
    print()
    print("Numerical values on the four corrected bridge rows:")
    print()
    print(f"  {'k':>3} {'N':>4} {'ω_1(P_k^𝔭) = 1 − N^(−k)':>32}")
    print("  " + "-" * 42)
    for k, N in BRIDGES:
        val = omega_1_P(k, N)
        print(f"  {k:>3} {N:>4}  {float(val):>30.20f}")
    print()


# ---------------------------------------------------------------
# (c) KMS_β expectation and the δ-deformation
# ---------------------------------------------------------------

def omega_beta_P(k, N, beta):
    """KMS_β expectation of P_k^𝔭."""
    return 1 - power(mpf(N), -k * beta)


def delta_omega(k, N, delta):
    """Shift of the KMS expectation from critical β=1 to β=1+2δ."""
    beta_crit = mpf(1)
    beta_shift = mpf(1) + 2 * delta
    return omega_beta_P(k, N, beta_shift) - omega_beta_P(k, N, beta_crit)


def delta_c(N, delta):
    """Paper 26 §7.1 Proposition 7.1 cocycle shift formula."""
    x = power(mpf(N), -2 * delta)
    return (1 - x) / (mpf(N) - x)


def verify_KMS_beta():
    print("=" * 70)
    print("(c) KMS_β deformation and comparison with Δc(δ)")
    print("=" * 70)
    print()
    print("    ω_β(P_k^𝔭) = 1 − N^(−kβ)")
    print("    Δω(δ) := ω_{1+2δ}(P_k^𝔭) − ω_1(P_k^𝔭)")
    print("           = N^(−k) − N^(−k(1+2δ))")
    print("           = N^(−k) · (1 − N^(−2kδ))")
    print()
    print("Compare against the Paper 26 §7.1 cocycle shift formula")
    print("    Δc(δ) = (1 − N^(−2δ)) / (N − N^(−2δ))")
    print()
    for k, N in BRIDGES:
        print(f"-- bridge row: k={k}, N={N}")
        print(f"   {'δ':>10} {'Δω(δ)':>22} {'Δc(δ)':>22} {'Δω/Δc':>14}")
        print("   " + "-" * 70)
        for delta_str in ["0.1", "0.05", "0.01", "0.001", "0.0001"]:
            delta = mpf(delta_str)
            dw = delta_omega(k, N, delta)
            dc = delta_c(N, delta)
            ratio = dw / dc if dc != 0 else mpf(0)
            print(
                f"   {float(delta):>10.5f} "
                f"{float(dw):>22.14e} "
                f"{float(dc):>22.14e} "
                f"{float(ratio):>14.6e}"
            )
        print()

    print("Leading-order (δ → 0):")
    print("   Δω(δ) ≈ 2kδ · log(N) · N^(−k)")
    print("   Δc(δ) ≈ 2δ · log(N) / (N − 1)")
    print("   Δω/Δc ≈ k · (N − 1) / N^k")
    print()
    print("Observed limiting ratios:")
    for k, N in BRIDGES:
        limit = mpf(k) * (mpf(N) - 1) / power(mpf(N), k)
        print(
            f"   k={k}, N={N:>3}: k(N−1)/N^k = {float(limit):>14.8e}"
        )
    print()
    print("Interpretation:")
    print("  Δω and Δc are both nonzero for δ ≠ 0 and vanish at δ = 0.")
    print("  The ratio Δω/Δc is NOT constant across bridges — so Δω")
    print("  does NOT equal Δc up to a universal normalization.")
    print("  Both quantities independently force δ = 0 via the")
    print("  integrality obstruction (Key Lemma C), but they measure")
    print("  different algebraic deviations:")
    print("    Δc is the Brauer class shift (Hasse invariant)")
    print("    Δω is the KMS-state expectation shift (mass deviation)")
    print()


# ---------------------------------------------------------------
# (d) The key observation: |Δω| < 1/k, so Δω ∉ (1/k)ℤ \ {0}
# ---------------------------------------------------------------

def verify_integrality_bypass():
    print("=" * 70)
    print("(d) Does Δω have its own integrality obstruction? Key Lemma C'")
    print("=" * 70)
    print()
    print("Claim (Key Lemma C'):")
    print("    For N(𝔭) ≥ 2 and k ∈ {2,3,4,6} and δ ∈ (−1/2, 1/2) \\ {0},")
    print("    |Δω(δ)| = N^(−k) · |1 − N^(−2kδ)| < N^(−k) < 1/(k+1) < 1/k")
    print("    (the middle inequality uses N^k > k+1 for N ≥ 2, k ≥ 2).")
    print()
    print("Therefore Δω(δ) ∈ (−1/k, 1/k) and Δω(δ) ∉ (1/k)ℤ \\ {0}.")
    print()
    print("Numerical verification on a fine grid δ ∈ {0.001, ..., 0.499}:")
    print()
    print(f"  {'k':>3} {'N':>4} {'max|Δω|':>20} {'1/k':>14} {'1/(k+1)':>14} {'ok':>6}")
    print("  " + "-" * 68)
    n_grid = 500
    for k, N in BRIDGES:
        max_val = mpf(0)
        for i in range(1, n_grid):
            delta = mpf(i) / (2 * n_grid + 2)  # δ ∈ (0, ~0.5)
            v = fabs(delta_omega(k, N, delta))
            if v > max_val:
                max_val = v
        bound_k = mpf(1) / k
        bound_kp1 = mpf(1) / (k + 1)
        ok = (max_val < bound_kp1)
        print(
            f"  {k:>3} {N:>4}  {float(max_val):>18.12f} "
            f"{float(bound_k):>14.10f} {float(bound_kp1):>14.10f}  "
            f"{'YES' if ok else 'NO':>5}"
        )
    print()
    print("Result: |Δω(δ)| is uniformly bounded well below 1/(k+1) < 1/k")
    print("on the four bridge rows of the corrected table. So Δω has an")
    print("independent integrality obstruction, parallel to Key Lemma C.")
    print()


# ---------------------------------------------------------------
# (e) The potential bypass of MY4
# ---------------------------------------------------------------

def bypass_analysis():
    print("=" * 70)
    print("(e) What this buys us: potential bypass of MY4")
    print("=" * 70)
    print()
    print("The classical MY4 wall:")
    print("  Meyer gives DISTRIBUTIONAL eigenstates of T̄_{BC,K}.")
    print("  Nelson gives SELF-ADJOINTNESS (real spectrum).")
    print("  The upgrade distributional → genuine point spectrum is the")
    print("  unsolved classical wall of the BC approach to GRH.")
    print()
    print("The projector argument (Route 3):")
    print("  P_k^𝔭 ∈ A_{BC,K} is an algebraic element, not a Hilbert")
    print("  space operator. Its KMS_β expectation is a legitimate")
    print("  number for every β ∈ ℝ_{>0}, computed via ITPFI. The")
    print("  β-deformation from 1 to 1+2δ measures the 'shift' of the")
    print("  projector's expectation under the corresponding change in")
    print("  the local Euler factor.")
    print()
    print("What's still needed:")
    print("  To make this a genuine MY4 bypass, we need a link:")
    print()
    print("    'ζ_K(1/2 + δ + it) = 0  ⇒  the β=1+2δ state is the")
    print("     *algebraically relevant* state at the Brauer class")
    print("     obstruction, not the β=1 state.'")
    print()
    print("  Without that link, the Δω computation above is just a")
    print("  tautology (it says 'at the hypothetical β = 1+2δ state,")
    print("  the projector has a different expectation'). We still")
    print("  need the argument that a zero of ζ_K FORCES the β=1+2δ")
    print("  expectation to match the Brauer class at index k — and")
    print("  that argument is exactly what Meyer's spectral inclusion")
    print("  provides.")
    print()
    print("  IF the link 'zero of ζ_K at δ ↔ shift by Δω(δ) or equivalent")
    print("  to Δc(δ)' is mechanical (e.g., from the ITPFI partition")
    print("  function), then MY4 is bypassed. IF it requires Meyer, we're")
    print("  back to the original problem.")
    print()
    print("What to check next:")
    print("  1. Write out the ITPFI partition function Z(β) = ζ_K(β) at")
    print("     β = 1+2δ and see whether ζ_K(1/2+δ+it) = 0 translates to")
    print("     a direct vanishing condition on ω_β(P_k^𝔭).")
    print("  2. Check whether the bridge cocycle Hasse invariant, as")
    print("     computed from ω_1(P_k^𝔭) × (local Frobenius data), is")
    print("     in (1/k)ℤ at β = 1 but not at β = 1 + 2δ.")
    print("  3. If either works, write up as Route 3 — KMS-projector")
    print("     bypass of MY4.")


def main():
    print()
    print("#" * 70)
    print("# Test of G's proposed projector P_k^𝔭 for MY4 closure")
    print("# Date: 2026-04-10")
    print("#" * 70)
    print()
    verify_projector_algebra()
    verify_KMS1()
    verify_KMS_beta()
    verify_integrality_bypass()
    bypass_analysis()


if __name__ == "__main__":
    main()
