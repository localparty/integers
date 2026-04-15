# D1.04 — Comparison to Connes' Programme

## The question

Connes has worked on RH via the BC system + trace formula for
25+ years. His approach uses Weil positivity, the trace formula,
and noncommutative geometry. Paper 13 claims to use CCM's
operators directly and close the convergence gap via Bögli +
Hurwitz. **Why should this different approach succeed where
Connes' has not?**

## What Paper 13 claims is different

1. **Direct construction vs spectral realization.** Connes'
   original approach (1999) tries to build a self-adjoint
   operator on ℋ_R whose spectrum is {γ_n}. This is the
   "spectral realization" programme. It is stuck at precisely
   the step of constructing ℋ_R and the operator.

   CCM's construction builds operators D_N directly on E_N^+
   (the Sonin/prolate spaces), bypassing the ℋ_R construction.
   Paper 13 takes these D_N as given and takes a limit.

2. **Convergence mechanism.** Connes' approach uses the trace
   formula as its convergence tool — relating the explicit
   formula for ζ to a distributional trace. Paper 13 uses
   ITPFI + Teschl + Bögli — a sequence-of-operators convergence
   argument.

3. **Hurwitz identification.** Connes uses Weil positivity to
   identify zeros. Paper 13 uses Hurwitz's zero convergence
   theorem. These are different tools.

## Is the approach "independent of Connes"?

**No.** CCM = **Connes**–Consani–Moscovici. Paper 13 builds on
the CCM construction, which IS Connes' current approach (2025
version). Paper 13 is **not independent of Connes**; it is
**downstream of Connes' latest work**.

The novelty claim in Paper 13 is narrower: the specific
synthesis of ITPFI → Teschl → Bögli → Hurwitz **closing the
convergence gap in CCM** is new. But the operators themselves
are Connes' (as co-author of CCM).

## Why hasn't Connes already done this?

Several possible reasons:

### (a) The convergence tools are very recent.

- Bögli 2017: relatively new spectral exactness result.
- Teschl–Wang–Xie–Zhou 2026: brand new gsrc simplification
  (**2026**, which matches Paper 13's date).
- The combination is genuinely novel.

If these tools only became available in 2026, Connes might
simply not have had time to combine them with his CCM
construction yet. This is **consistent with Paper 13's framing**.

### (b) The convergence-from-finite-N is more tractable than spectral-realization-directly.

Connes' original approach (1999) tries to build ℋ_R and the
operator directly. CCM's approach builds approximations and
takes a limit. The latter is *in principle* easier — convergence
arguments are more flexible than direct constructions. Paper 13
leverages this.

### (c) The honest accounting: maybe Connes has seen this and it doesn't work.

A pessimistic reading: Connes is probably aware of Bögli and
Teschl. If the combination worked trivially, the CCM paper
itself would have included it. That it did not might mean
Connes saw a technical obstruction.

Paper 13's response (implicit): "the CCM paper is very recent,
and the synthesis happens to be the kind of thing a second team
can do in parallel". Possible but not decisive.

## The 25-year obstacle ("the wall")

Paper 13 Section 13.2: "**The one wall.** ℋ_1 has spectrum
{log n}. ℋ_R (if it exists) has spectrum {γ_n}. No bridge
between them exists without assuming the answer."

Paper 13 claims CCM bypasses this by "building operators whose
spectra *approximate* {γ_n} directly". This is a genuinely
different strategy from the ℋ_R construction.

However, the wall's "no bridge without assuming the answer"
content is about the **spectrum identification**, not the
existence of the operator. The CCM operators exist (finite-dim,
concretely constructed). The question is whether their limit
spectrum is really {γ_n}.

Paper 13's Hurwitz argument answers this: yes, the Fourier
transforms converge to Ξ, so the spectra converge to zeros of Ξ.
But this is only possible because Ξ is **defined** using ζ, which
brings the zeros in as a target. This is **not** circular (since
the limit is a theorem, not an assumption), but it is adjacent
to the kind of self-referencing that Connes has been navigating.

## Is the novelty genuinely new?

Yes, **with caveats**:

- The four ingredients (ITPFI, Teschl, Bögli, Hurwitz) have never
  before been combined to close the CCM convergence gap. That is
  new.

- Each ingredient is independently established (ITPFI is a
  standard BC result; Teschl, Bögli, Hurwitz are in the
  literature). The combination is the innovation.

- Whether the combination **succeeds rigorously** is the question
  of this review. My assessment: the combination is the right
  sort of thing, but the execution has enough interface gaps
  (Section D1.03) that it is currently at the level of "strong
  plausibility" rather than "rigorous proof".

## Verdict on this subpoint

The approach is **structurally different** from Connes' 1999
trace-formula programme, in that it routes through explicit
finite-dim operators and a convergence theorem rather than a
direct spectral realization. This is legitimate.

**But the approach is NOT independent of Connes**: it builds on
CCM (co-authored by Connes) as its Layer 1.

**Why it might succeed:** (i) the Teschl 2026 simplification and
Bögli 2017 spectral exactness are recent tools that enable a
sequence-of-operators approach; (ii) the CCM construction
provides concrete finite-dim operators to apply them to;
(iii) Hurwitz provides the identification step.

**Why it might not (yet):** the synthesis is novel and the
interfaces are not all rigorous; the 8/10 self-assessment
reflects real remaining work.

A fair characterization: Paper 13 is **an attempt to complete
Connes' latest approach**, not a parallel route. The success or
failure depends on whether the closing arguments (Layers 3–5)
are actually watertight. They are currently not.
