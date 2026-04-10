# D1.03 — Interface Gaps

## The tools combined

Paper 13 synthesizes tools from six distinct areas:

| Layer | Tool | Source |
|:------|:-----|:-------|
| 1 | CCM zeta spectral triples | Noncommutative geometry (Connes 2025) |
| 2 | ITPFI factorization | Operator algebras (BC 1995 + AW 1968) |
| 3 | Archimedean / PNT / Davis-Kahan | Classical analysis + perturbation theory |
| 4 | Teschl gsrc + Bögli spectral exactness | Modern spectral theory |
| 5 | Hurwitz zero convergence | Classical complex analysis |

At each interface there is a translation step. I enumerate them.

## Interface 1: CCM → ITPFI

**Translation:** The CCM operators D_N are built from the Weil
distribution and Fourier basis. The ITPFI factorization is a
property of the KMS_1 state on the BC algebra. What connects them?

Paper 13 Section 4.6 asserts:

> "The CCM operators D_N are finite-rank truncations of a
> function of H_{ω_1} = modular Hamiltonian of ω_1."

This is an assertion without proof. The modular Hamiltonian of
ω_1 is H = −log Δ_{ω_1} = Σ_p log(p)·N_p where N_p is the p-local
number operator. The CCM operators D_N are built from a different
object (the Weil distribution on an interval). The identification
"D_N is a finite-rank truncation of a function of H" is not
obviously true and is not proved.

**Gap:** The structural tie between CCM and ITPFI is asserted, not
established.

## Interface 2: ITPFI → Teschl

Already discussed in B3.01 and A2.03: ITPFI gives entry-by-entry
stabilization; Teschl wants pointwise form convergence on a
common form domain. The translation requires:

- Density of the algebraic direct limit in the form domain
  (asserted via Chebyshev completeness; not rigorously tied to
  the form topology),
- Extending the convergence from the direct limit to the form
  domain,
- Supplying the relative form bound (not from ITPFI, from CF
  decay).

**Gap:** The translation is informal.

## Interface 3: Teschl → Bögli

Teschl gives gsrc. Bögli wants strong resolvent convergence (or
gsrc) for sequences of operators on Hilbert spaces. The questions:

- Does Bögli's theorem cover gsrc or only ordinary srg?
- Does Bögli cover sequences on varying Hilbert spaces, or only
  on a common H?

I cannot verify from Paper 13's exposition.

**Gap:** The translation is implicit.

## Interface 4: Bögli → Hurwitz

Bögli gives Hausdorff convergence of spectra on compact subsets.
Hurwitz wants uniform convergence of *functions* (ξ̂_N) on compact
subsets, not of their zero sets.

These are **different statements**. One can have spectral
convergence (zero set converges in Hausdorff) without function
convergence (the functions themselves need not be close).

Paper 13 bridges this via CCM Theorem 5.10(iii): "zeros of ξ̂_N
= eigenvalues of D_N". This gives:
- Spectral convergence (from Bögli) ↔ zero-set convergence,
- But to apply Hurwitz we need function convergence.

Paper 13 establishes function convergence **separately** (Theorem
10.1 via Estimate (b) + CCM Lemma 7.3), not via Bögli.

**So Bögli and Hurwitz are actually independent inputs**, both
needed. Bögli tells us D_∞ has the "right" finite-limit spectrum;
Hurwitz tells us this spectrum is exactly {γ_n} (because ξ̂_N →
Ξ uniformly). Without Bögli, one might worry that the Hurwitz
limit identifies a different operator's spectrum; without
Hurwitz, one might worry that Bögli's limit spectrum is not
{γ_n}.

OK this is structurally fine. The paper correctly uses both.

**Less of a gap here, more an exposition point.** Paper 13 should
clarify that Bögli and Hurwitz serve different purposes.

## Interface 5: Hurwitz → RH

The conversion from "zeros of Ξ in the strip are real" to "RH
holds" requires:

- Zeros of Ξ in {|Im z| < 1/2} are in bijection with non-trivial
  zeros of ζ in the critical strip,
- The Xi function captures all such zeros.

These are standard facts about ξ and Ξ. Paper 13 Section 10.4
glosses over them but they are correct.

**No gap at this interface.**

## Summary

The proof has **multiple informal interfaces**. The most worrying
are Interfaces 1 (CCM ↔ ITPFI) and 2 (ITPFI ↔ Teschl), because
they involve non-trivial algebraic structure translations that
are asserted rather than proved.

**Interface 3 (Teschl ↔ Bögli)** has a specific technical question
(gsrc vs srg, varying Hilbert spaces) that would need to be
resolved by reading the Teschl and Bögli papers carefully.

**Interface 4 (Bögli ↔ Hurwitz)** is clean in principle —
the two serve complementary purposes — but Paper 13's exposition
does not clearly distinguish them.

**Interface 5 (Hurwitz ↔ RH)** is fine in principle but not
properly exposed (see D1.02).
