# Summary — Run r02

*Advanced Mathematical Referee, Paper 13 (v2: CCM + ITPFI + Bögli + Hurwitz).*
*Written 2026-04-10.*

---

## The proof in one sentence

Paper 13 claims that the Riemann Hypothesis follows from
Connes–Consani–Moscovici's 2025 zeta spectral triples (which
construct self-adjoint operators D_N whose spectra approximate
the Riemann zeros) combined with a novel convergence mechanism
(ITPFI state factorization → Teschl form-boundedness → Bögli
spectral exactness → Hurwitz zero convergence) that closes the
limit N → ∞ and identifies the limit spectrum with {γ_n}.

---

## My headline verdict

**The proof is architecturally correct but not rigorously
executed.** Every layer of the chain names the right tool for its
purpose, and the tools, individually, are legitimate. But
concrete rigor gaps in Layers 3, 4, and 5 — combined with a
tautological final deduction in Section 10.4 and a cosmetic but
telling error in Ξ(0) — prevent me from certifying the preprint
as a proof of RH.

The paper's self-rating of 8/10 is **approximately right in
spirit** but **over-estimates the independence of Layers 2–6
from CCM**. A more honest rating would be **6–7/10 as written**,
with a clear path to 8/10 via revisions and to 9/10 if CCM is
refereed.

---

## Required closing statements

### 1. CCM dependency

**Verdict:** The proof is **conditional on CCM (arXiv:2511.22755)
being correct**, and is not acceptable as an unconditional proof
of RH in its current form.

The honest framing is: "Assuming the results of Connes–Consani–
Moscovici 2025 — specifically Theorems 4.2, 5.10, and Lemmas
7.2, 7.3 — the Riemann Hypothesis holds." Paper 13's Theorem 1.1
should be restated this way. As written, it over-claims.

CCM is by Connes, Consani, and Moscovici. Connes is the world's
leading authority on the noncommutative-geometric approach to RH.
CCM is nonetheless an unrefereed 2025 preprint, and Paper 13
adds an **even-sector modification** (restricting to E_N^+) whose
compatibility with CCM's Theorem 5.10 is asserted but not proved.
The compound risk is:

  (CCM preprint error) × (even-sector compatibility not verified).

The paper labels this 8/10. I concur that refereeing CCM would
move to 9/10. Independent verification of CCM's results on the
even sector, combined with the other fixes below, would move to
10/10.

### 2. Teschl–Bögli synthesis

**Verdict:** The combination of Teschl's gsrc simplification
(arXiv:2601.10476) with Bögli's spectral exactness (arXiv:
1604.07732) in the CCM zeta-spectral-triple context is
**genuinely novel and has interface gaps that are not resolved
rigorously in the preprint**.

Specifically:

- **Teschl Lemma 2.7 applied to Galerkin sequences on varying
  Hilbert spaces** is not explicitly verified against Teschl's
  actual paper. The lemma may or may not cover the Galerkin case;
  Paper 13 assumes it does.

- **The "form difference" δ_N := Q_N − P_N Q_∞ P_N** (Definition
  9.2) is not the same as Q_N − Q_∞ on the common form domain.
  Paper 13's bound ‖Δ_N‖ ≤ C ρ^{−N} is established on the
  Galerkin-projected residual, not on Teschl's full hypothesis.

- **KLMN closability of Q_∞** (Corollary 9.6) is argued via the
  incorrect implication "lower-boundedness ⇒ closability". This
  is false in general. A rigorous argument would cite specific
  Reed–Simon results from Chapter X and check the three KLMN
  conditions separately.

- **The rank-one stabilization bound ‖Δ_N‖ ≤ C ρ^{−N}** is
  attributed to research/40 Lemma 1, **which is not in the
  preprint**.

- **Theorem 7.1's proof** of the uniform H¹ bound uses the
  algebraic inequality "(1+a²x²)/(x²+1) ≤ a² for x ∈ ℝ when
  a ≥ 1", which I verified computationally holds iff
  2π/L ≥ 1, i.e., iff **λ ≤ e^π ≈ 23.14**. At the paper's
  numerical λ = √14 ≈ 3.74, the bound holds comfortably; at any
  larger λ, the proof breaks. The paper does not discuss this
  restriction or its implications for any "uniform in λ" reading
  of the theorem.

This interface gap cluster is the **single biggest concern I
have about the proof**. It is Layer 4, and Layer 4 is the hinge
between Layers 2–3 (inputs) and Layer 5 (Hurwitz output). If
Layer 4 is not rigorous, the chain is not a chain.

### 3. The Hurwitz upgrade / final deduction

**Verdict:** The Hurwitz step is **structurally correct and is
the right tool**, but the **final deduction in Section 10.4 Step
4 is tautological as written**, and the logically sufficient
version of the argument is never made explicit.

The paper writes:

  "{γ_n} = spec(D_∞) ⊂ ℝ. Therefore γ_n ∈ ℝ for all n."

This is tautological: the {γ_n} are *defined* in Section 1
notation as "the imaginary parts of the non-trivial zeros on the
critical line". So γ_n ∈ ℝ is trivially true and contains no
information about off-line zeros.

The correct argument is:

  (i) Lemma: each ξ̂_N has only real (complex-plane) zeros.
      [Proof: CCM Theorem 5.10(iii) + the explicit sine-times-
      rational formula.]

  (ii) By Estimate (b) + CCM Lemma 7.3, ξ̂_N → Ξ uniformly on
       compact subsets of {|Im z| < 1/2}.

  (iii) Ξ(0) ≠ 0 (actually Ξ(0) ≈ 0.4971, **not** the "1/2"
        Paper 13 claims in Sec 10.3 and App E.4).

  (iv) By Hurwitz, every zero of Ξ in {|Im z| < 1/2} is a limit
       of zeros of ξ̂_N. Since each ξ̂_N has only real zeros,
       such limits are real.

  (v) Zeros of Ξ in {|Im z| < 1/2} correspond via s = 1/2 + iz
      to non-trivial zeros of ζ in 0 < Re s < 1.

  (vi) Therefore every non-trivial zero of ζ is on Re s = 1/2.
       RH.

**Paper 13 has all the ingredients but does not assemble them
this way.** A referee is left to reconstruct the argument, which
is the referee's job only up to a point. For a Clay-millennium
proof, the substantive deduction must be explicit in the paper.

The L² → uniform convergence upgrade via Paley–Wiener / Cauchy–
Schwarz (Corollary 6.6) is fine at fixed N. The persistent
concern is that Paper 13 uses "as λ → ∞" language in Sections
5–6 while the downstream Bögli limit is "as N → ∞". This λ-vs-N
conflation obscures whether the uniform convergence holds in
the limit that is actually taken.

### 4. AE simplicity sufficiency

**Verdict:** **The certified computation at N = 1, …, 20 is
rigorous** (120-digit mpmath, 10^{72} safety margin). The
**extension to N > 20 via the "Slepian limit" is heuristic, not
a theorem**.

The Slepian-limit argument in Section 12.3 asserts operator
convergence A^{ev}(λ, N) → prolate spheroidal wave operator, but
does not prove it. It argues that the limiting overlap is
positive (true for Slepian ground states + positive cosh kernel)
and invokes "continuity" to conclude f_N(√14) > 0 for large N.
Continuity requires a convergence theorem that is not in the paper.

For the proof chain, simplicity at λ = √14 is needed at every N
(because the Bögli limit is taken at fixed λ = √14). The
certification covers N ≤ 20; above this, the argument is not
rigorous.

**A refereeable version would need either**:

(a) A rigorous operator-convergence theorem proving the Slepian
    limit and its consequences for f_N, or

(b) A precision-scalable certification at arbitrarily large N
    (expensive: precision must grow linearly in N due to the
    exponentially shrinking spectral gap), or

(c) A fundamentally different sufficiency argument that does
    not rely on per-N simplicity.

Currently, none of these is in the paper.

### 5. Comparison to Connes' programme

**Verdict:** Paper 13 is **not independent of Connes' programme**;
it builds on the CCM construction (Connes-Consani-Moscovici
2025), which is the current phase of Connes' 25+ year effort.

What Paper 13 adds is the closure mechanism: ITPFI state
factorization (standard operator-algebraic result), Teschl's
2026 gsrc simplification, Bögli's 2017 spectral exactness,
and classical Hurwitz. The **synthesis** is new; the
**components** are not.

Why hasn't Connes already done this? Plausible reasons:

- The CCM paper (2025) and Teschl's gsrc simplification
  (2026) are both very recent. The synthesis window is narrow.
- Connes may have seen a technical obstruction that Paper 13's
  authors are not yet aware of. I cannot determine this from
  the preprint alone.
- A more optimistic reading: Paper 13 found a route that
  Connes simply hasn't had time to combine yet. This is
  consistent with the recent dates.

For the chain to succeed where Connes has not, Paper 13 must
rigorously execute the synthesis. Currently, the execution has
gaps at Interfaces 1 (CCM ↔ ITPFI), 2 (ITPFI ↔ Teschl), 3
(Teschl ↔ Bögli), and 5 (Hurwitz ↔ final deduction). These are
fixable in principle, but not yet fixed.

**My judgment:** Paper 13 is a **good-faith attempt to close
Connes' current approach**. Whether it succeeds depends on
closing the gaps listed above. It is not currently a proof of
RH; it is a promising architecture with multiple remaining
technical and exposition items.

---

## Overall Assessment

**Is the Riemann Hypothesis proved?**
No. The proof is conditional on CCM (arXiv:2511.22755), and even
under that assumption, there are concrete rigor gaps in Layers
3, 4, 5, and in the final deduction in Section 10.4 Step 4. The
paper's architecture is right; its execution is incomplete.

**The single most critical issue:**
The final deduction in Section 10.4 Step 4 is tautological as
written, and the logically sufficient argument — Hurwitz in the
complex plane applied to the real-zero property of ξ̂_N — is
implicit but never explicit. Without a rewrite making this
argument explicit, the paper does not prove RH even if every
other ingredient is correct.

**Clay Prize Eligibility:**
**Not eligible** at present. Specific obstacles:

- Theorem 1.1 is stated as unconditional but the proof
  fundamentally depends on an unrefereed preprint
  (arXiv:2511.22755). Clay requires publication in a qualifying
  outlet (Clay rules §6), which CCM does not currently satisfy.

- Clay requires "general acceptance in the global mathematics
  community" (§4(c)) and a 2-year waiting period (§4(b)). Paper
  13 is new (2026-04-10).

- Clay requires the proof to address the specific questions in
  the official description (§5(d)). Paper 13 engages with the
  Hilbert–Pólya / Connes trace-formula approach, which Bombieri
  cites, but does not discuss L-functions and GRH — also
  highlighted in Bombieri's description.

- The "rigorous mathematics throughout" standard (implicit in
  §5(a) "complete mathematical solution") is not met: there are
  at least 8 concrete rigor gaps (see CL3), including the
  tautological final deduction, the broken Theorem 7.1 at λ >
  e^π, and the incorrect KLMN closability implication.

Even a refereed version of CCM would not make Paper 13 eligible;
the paper itself needs substantial revision.

**The three most critical issues (ranked):**

1. **The final deduction in Section 10.4 Step 4 is tautological
   as written.** The correct Hurwitz-in-ℂ + real-zero-property
   argument is never explicit. Without this fix, the proof is
   not a proof.

2. **The Teschl–Bögli synthesis in Layer 4 has multiple interface
   gaps** — informal application of Teschl Lemma 2.7 to Galerkin
   sequences, an incorrect KLMN closability implication, and a
   load-bearing estimate (‖Δ_N‖ ≤ C ρ^{−N}, research/40 Lemma 1)
   not included in the preprint. The synthesis is novel and
   consequently unvetted.

3. **Theorem 7.1 proof step (7.5) is valid only for λ ≤ e^π ≈
   23.14**, a restriction the paper does not discuss. At the
   paper's numerical λ = √14 the bound holds; any uniform-in-λ
   reading of the theorem is broken. This is a concrete technical
   finding I verified computationally.

**What would close the gaps (if any):**

A revision that:

1. Rewrites Section 10.4 Step 4 to state explicitly the Hurwitz
   argument using the real-zero property of ξ̂_N (with the
   real-zero property stated and proved as a named lemma).

2. Includes research/40 Lemma 1 (with full proof) and research/
   20, 24, 37 estimates (or replaces them with proofs in the
   preprint itself).

3. Corrects Theorem 7.1 by either (a) restricting λ explicitly
   to ≤ e^π or (b) reproving the uniform H¹ bound for
   arbitrary λ.

4. Corrects the KLMN closability argument to cite specific
   Reed–Simon II Chapter X results and separately verify the
   three conditions (dense domain in the form norm, closability,
   lower boundedness).

5. Rigorizes the Slepian-limit extension to N > 20 as a
   convergence theorem about A^{ev}(λ, N) → prolate operator
   with eigenvector continuity.

6. Reframes Theorem 1.1 as conditional on CCM.

7. Disambiguates the parameter λ throughout (bandwidth vs
   spectral parameter) with consistent usage.

8. Fixes cosmetic errors (Ξ(0) in Section 10.3 and Appendix
   E.4; the divergent PNT-tail estimate in Section 6 / Lemma
   6.3).

9. Proves the even-sector restriction compatibility with
   CCM's Theorem 5.10.

After these fixes, **and** CCM being refereed, **and** an
independent third party verifying Layers 2–6, the proof would
be eligible.

**Comparison to Connes' programme:**

Paper 13 is an attempt to complete Connes' current approach,
not an independent route to RH. Its Layer 1 is the CCM
construction, which is Connes' 2025 work with Consani and
Moscovici. What Paper 13 contributes is the convergence closure:
ITPFI (standard BC result) + Teschl 2026 (new) + Bögli 2017 +
classical Hurwitz, assembled in a way no prior paper has
assembled them. The synthesis is novel; the components are
established.

Whether this approach succeeds where Connes' 25-year trace-
formula effort has not depends entirely on whether the synthesis
is executed rigorously. Currently, the execution has gaps. With
revisions closing the gaps listed above, the synthesis becomes
a plausible route. Without them, the paper is an announcement
of an approach rather than a proof.

The "25-year obstacle" framing (Paper 13 Section 13.2: "ℋ_1 has
spectrum {log n}; ℋ_R has spectrum {γ_n}; no bridge without
assuming the answer") is mostly accurate. CCM bypasses this
obstacle by constructing finite-dimensional operators whose
spectra *approximate* {γ_n} directly. Paper 13 then uses
convergence tools to take the limit. The novelty is this
"approximate + limit" architecture, which is legitimately
different from the ℋ_R spectral-realization programme.

However, the attempt rests on a **single preprint** (CCM 2025),
and that preprint has not been vetted. Paper 13's 8/10 rating
honestly acknowledges this dependence. My rating — 6-7/10 as
written, rising to 8/10 after the revisions above — reflects
both the CCM dependence and the additional rigor and exposition
gaps I identified.

---

## Final note

This is the most carefully constructed claimed proof of RH I
have seen in the past two years. The architecture is thoughtful,
the tools are appropriate, the adversarial self-review is
admirable, and the honest-accounting section is honest in spirit.

But it is not yet a proof. The gaps are fixable. The work to fix
them is concrete and bounded. I estimate that a focused revision
closing the items in the "what would close the gaps" list above
would take several months of dedicated effort, and that the
result would be a refereeable conditional proof (conditional on
CCM). If CCM is then refereed, it would become an unconditional
proof.

Paper 13 is not that refereeable version. It is the state before.
