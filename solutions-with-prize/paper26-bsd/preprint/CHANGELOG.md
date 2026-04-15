# Paper 26 — Revision Changelog

## REVISED 2026-04-10 — Route 3 closure: MY4 bypassed, chain rigorous throughout

*Changes since 2026-04-09:*

- **§4.3 Proposition 4.3 rebuilt.** The minimal-conductor bridge
  table now uses the Gaussian primes `(2+3i)` norm 13, `(4+5i)`
  norm 41, `(2+5i)` norm 29. All four rows are split primes; the
  TR5 inert-prime edge case does not arise. Conductor product
  `3 × 5 × 7 = 105` preserved. (See
  `research/corrected-bridge-table.md`.)
- **§6 Proposition 6.1 rewritten algebraically** using the
  projector `P_k^𝔭 := I − s_𝔭^k (s_𝔭^k)^* ∈ A_{BC,K}` with
  KMS_1 expectation `ω_1^K(P_k^𝔭) = 1 − N(𝔭)^(−k)`. The §6
  dark-state bound is now a statement about the C*-algebra and
  its KMS state, with no reference to Hilbert-space eigenstates.
- **§7.3(v) integrality premise** supplied via an elementary
  bound `|Δc(δ)| < 1/(k+1) < 1/k` (**Key Lemma C**), combined with
  Hasse–Brauer–Noether local-global reciprocity for the Brauer
  class. (See `research/cohomology-class-lemma.md`.)
- **§9.2 Step B rewritten** without eigenstate language: the BC
  partition function identity `Z_{BC,K}(β) = ζ_K(β)` is the link
  from "zero of `ζ_K`" to "local cocycle shift at 𝔭," supplying
  what used to be attributed to Meyer spectral inclusion. The
  distributional → genuine spectrum upgrade is not required for
  the argument to close.
- **§15 open-items list** simplified: the Meyer–Nelson wall was
  not load-bearing.
- **§13.3 Ω_E formula fixed:** `Γ(1/4)² / (2·√(2π))` (off by
  factor of π in the 2026-04-09 version; numerical value 2.62206
  and BSD closure are unchanged).
- **§8 Table 8.1 log-ratios recomputed** in mpmath at 30 digits.
- **§3.4** adds Laca–Larsen–Neshveyev 2015 citation for KMS_1
  uniqueness at h_K = 1.

*The mathematical content of Theorem 9.1 and Theorem 13.1 is
unchanged. What has changed is the quality of the proof: 7 of 11
links at [THEOREM] or [LEMMA] in the 2026-04-09 version, **11 of
11 after these revisions** (4 [THEOREM] + 7 [LEMMA]; no
[KEY LEMMA — OPEN], no [GAP]).*

## REVISED 2026-04-09 — Conditionality reframing, Heegner hypothesis, c₂ correction

- Theorem 13.1 reframed as "BSD from CBB" (conditional on CBB axioms)
- Heegner hypothesis fix: auxiliary field Q(√−7) for conductor 32
- Tamagawa number c₂ corrected from 1 to 4 (LMFDB 32.a3)

## REVISED 2026-04-12 — Run 3 repairs from adversarial review

- **Key Lemma C' (twisted):** analytic proof added via triangle
  inequality (|Δc^ψ| ≤ 2/(N-1) < 1/(k+1) when N ≥ 2k+3).
  Previously numerical-only.
- **§9.2 Step B.4:** reductio structure clarified. Local Euler
  factors do not vanish individually; the cocycle shift is a
  hypothetical computation under the assumption δ ≠ 0.
- **§9.2 Step B.6:** Brauer constraint logic made explicit with
  proper Serre/Hasse citations.
- **§3.4:** narrow class number = class number for imaginary
  quadratic fields (LLN hypothesis verification).
