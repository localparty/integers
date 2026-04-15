# D2.05 — Comparison to Connes' Programme (D2 view)

## What Connes has done on RH

- **Connes 1999** ("Trace formula in noncommutative geometry
  and the zeros of the Riemann zeta function"). The spectral-
  realization approach: build a Hilbert space ℋ_R and an
  operator R whose spectrum encodes the zeros. Uses the
  Bost-Connes system, the trace formula, and Weil positivity.
  **Status: incomplete.** Connes acknowledges the spectral-
  realization step has not been closed.

- **Connes-Marcolli 2008** (*Noncommutative Geometry, Quantum
  Fields and Motives*). A textbook treatment of the
  programme. Same incompleteness.

- **CCM 2025** (Connes-Consani-Moscovici, arXiv:2511.22755).
  The zeta spectral triples approach. Builds finite-dim
  operators D_N whose spectra approximate Riemann zeros to
  10^{−55} at N = 6. **Status: preprint, not refereed.**

- **Connes-van Suijlekom 2025** (arXiv:2511.23257, CMP). The
  Hurwitz application to the Xi function. Establishes uniform
  convergence of eigenvector Fourier transforms to Ξ on compact
  substrips (this is CCM Lemma 7.3 in Paper 13's citations).

So the "Connes programme" has three phases:
1. Classical (1999-2024): trace formula, spectral realization.
2. CCM (2025): finite-dim approximation.
3. Closure (???): taking the limit.

Phase 3 is what Paper 13 attempts.

## Is Paper 13 "closing" Connes' programme?

Paper 13 uses CCM as its Layer 1 (Connes' 2025 phase). The
contribution is the closure mechanism (ITPFI + Teschl + Bögli +
Hurwitz).

**In that sense, Paper 13 is part of Connes' programme, not
independent of it.** The synthesis is new, but the foundation is
Connes-Consani-Moscovici's.

**Why hasn't Connes already done the closure?** Possible
explanations:

1. CCM is very recent (2025). The convergence tools (Teschl 2026)
   are even newer. The synthesis window is narrow.

2. Connes might be working on closing his own gap through a
   different route (e.g., trace formula, Weil positivity) and
   has not considered the Teschl-Bögli route.

3. There may be a technical obstruction Connes has seen that is
   not obvious to Paper 13's authors. If CCM's Theorem 5.10 has
   subtleties that the preprint does not fully capture, Connes
   might be aware.

## The "we closed what Connes could not" framing

Paper 13's Strategy 26 and Section 14 frame the work as
"closing the CCM gap" — the gap being the passage from finite N
to the limit and the identification of the limit spectrum with
{γ_n}.

This framing is accurate **if** Paper 13's Layers 2-5 actually
close the gap rigorously. As analyzed in D2.04, they do not
**yet** — there are fixable rigor gaps. So the accurate framing
would be:

> "We propose a route to closing the CCM gap via
> ITPFI + Teschl + Bögli + Hurwitz. The route is structurally
> complete. Several technical items remain to be rigorized."

Instead, Paper 13 frames it as:

> "We close the CCM gap. The Riemann Hypothesis follows."

These are different claims. The former is accurate; the latter
is overstated.

## Would Connes accept Paper 13's proof?

**Hypothetical.** If Connes read Paper 13 carefully, I expect he
would:

1. **Accept Layer 2 (ITPFI)** as correct — he knows the BC
   system better than anyone.

2. **Have concerns about the even-sector modification** — it
   is Paper 13's addition to CCM, and Connes would want to see
   the compatibility checked.

3. **Have concerns about the Teschl-Bögli synthesis** — it is
   genuinely novel, and Connes would want to see the interface
   gaps closed (especially Galerkin on varying Hilbert spaces).

4. **Have concerns about Section 10.4's final deduction** — he
   would see immediately that the stated argument is tautological
   and demand a rewrite.

5. **Have concerns about internal research notes** — a published
   proof cannot rest on unpublished material.

In short: Paper 13's architecture would likely be accepted by
Connes as *promising*, but the current execution would not pass
his own scrutiny without revision. This is consistent with the
paper's self-rating of 8/10.

## Verdict on this subpoint

**Paper 13 is not independent of Connes** — it builds on CCM
(which is Connes-Consani-Moscovici). The closure mechanism is
new, but the foundation is Connes' 2025 work.

The question "why hasn't Connes done this" has a mundane
answer (CCM and Teschl are both very recent) and a cautionary
answer (Connes may have reasons to not be confident about the
Teschl-Bögli route that Paper 13 does not yet appreciate).

A final judgment requires Connes' own reading of Paper 13, which
I cannot supply here. From a referee's perspective, I mark this
as **Paper 13 is a good-faith attempt to close Connes' current
approach, with acknowledged and unacknowledged gaps.**
