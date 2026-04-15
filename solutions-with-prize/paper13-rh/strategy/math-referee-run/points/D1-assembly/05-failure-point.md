# D1.05 — The Most Likely Failure Point

## Ranking the risks

Based on the analysis in A1–C2 and D1.01–04, here is my ranking
of where the proof is most likely to fail.

### Rank 1: Teschl–Bögli synthesis (Layer 4)

**Why it's the biggest risk:**

- The synthesis is genuinely novel — ITPFI + Teschl + Bögli in
  this configuration has no precedent.
- Multiple interface gaps (KLMN closability, form-bound
  definition, Galerkin on varying Hilbert spaces).
- The load-bearing estimate ‖Δ_N‖ ≤ C·ρ^{−N} is not in the
  preprint (research/40 Lemma 1).
- Theorem 7.1 (uniform H¹ bound) has a proof that only works
  for λ ≤ e^π ≈ 23.14, a restriction not discussed.

**What would break it:** any one of: (a) Teschl Lemma 2.7 does
not cover Galerkin sequences on varying Hilbert spaces; (b)
Q_∞ is not closable, so the Friedrichs extension fails; (c)
research/40 Lemma 1's decay rate is wrong; (d) the H¹ uniform
bound is not uniform in N.

### Rank 2: Final deduction (Section 10.4)

**Why it's a major risk:**

- The stated argument is tautological (γ_n are defined as
  imaginary parts of critical-line zeros; concluding γ_n ∈ ℝ
  adds nothing).
- The correct argument (Hurwitz + real-zero property of ξ̂_N)
  is never explicit.
- A reader cannot reconstruct the intended proof from Section
  10.4 alone.

**What would break it:** the correct argument might simply not
be what the authors intended, and the paper's argument may be
flawed in a different way than I reconstructed. Without an
explicit statement, I cannot be sure.

### Rank 3: CCM preprint error

**Why it's a significant risk:**

- CCM is a 2025 unrefereed preprint.
- Three CCM results are load-bearing (Theorem 4.2,
  Theorem 5.10(iii), Lemma 7.3).
- A subtle error in any of these propagates.
- Especially for Theorem 5.10(iii) (the zero–spectrum
  identification), a hidden hypothesis or domain issue could
  break things.

**What would break it:** the next author who reads CCM
critically finds an error. This is outside Paper 13's control.

### Rank 4: Even-sector modification

**Why it's a notable risk:**

- Paper 13 imposes the even-sector restriction E_N^+ as a
  modification of CCM's construction.
- The compatibility of this modification with CCM's Theorem
  5.10 is asserted but not proved.
- If CCM's theorem fails under the restriction, the whole
  foundation shifts.

**What would break it:** the restricted operators don't satisfy
the hypotheses of CCM Theorem 5.10 cleanly (e.g., the rank-one
perturbation has issues, or the radical structure is different).

### Rank 5: AE simplicity for N > 20

**Why it's a medium risk:**

- The Slepian-limit argument is heuristic, not a theorem.
- Finite certification exhausts at some N_max (because
  precision must grow with N due to gap shrinkage).
- If simplicity fails at infinitely many N, CCM Theorem 5.10
  doesn't apply at those N, and the Hurwitz convergence is
  compromised.

**What would break it:** the Slepian convergence argument, when
made rigorous, doesn't actually hold, or the ground-state
overlap has non-monotone behavior and dips through zero at some
N > 20.

### Rank 6: Eigenvector approximation (Theorem 6.4)

**Why it's a lower risk:**

- The Davis-Kahan structure is correct; the PNT slip is probably
  an exposition error, not a substance error.
- The constants are "certified" in internal research notes
  (research/20, 24, 37) that a referee would need to read.
- The λ-vs-N uniformity is not established, but this is a
  shared concern with Layer 4.

**What would break it:** the gap lower bound gap(T_0) ≥ C''·λ
turns out to be wrong or to depend on N in a way that degrades
with the Boegli limit.

### Rank 7: Archimedean estimate

**Why it's a lower risk:**

- The Stirling-type asymptotic for the archimedean scalar is
  correct.
- The lower bound on the p-adic sum is heuristic but aligned
  with the explicit formula.
- Downstream uses the bounds in a way that only needs the
  shape, not precise constants.

**What would break it:** an unexpected issue in the operator-norm
translation from scalar asymptotics.

## The single most critical issue

**Rank 1 (Teschl–Bögli synthesis) and Rank 2 (final deduction)
are tied for most critical.**

Rank 1 is a mathematical gap: specific technical items are not
rigorous. Fixing them is concrete work but the tools are there.

Rank 2 is an exposition gap: the correct argument is implicit
but not stated. Fixing it requires rewriting Section 10.4 to
make the Hurwitz-in-ℂ + real-zero-property argument explicit.

If I had to name one single issue: **the proof's final
deduction as written in Section 10.4 Step 4 is tautological.
The substantively correct argument is not in the paper.** This
is the single most important exposition fix. Without it, the
paper reads as "operators converge, spectrum is real, therefore
γ_n is real" — which is trivial because γ_n are real by
definition.

## Verdict on this subpoint

The proof is **not** most likely wrong at CCM — that's an
external risk and likely manageable. The proof is **most likely
inconclusive** at Section 10.4 (exposition) and at Layer 4
(rigor of Teschl-Bögli synthesis).

If Section 10.4 is rewritten explicitly and Layer 4's technical
gaps are closed, the proof is likely correct conditional on CCM.
As written, it is not.
