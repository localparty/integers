# D2.01 — Conditionality

## Is the proof stated as conditional on CCM?

Theorem 10.3 / Theorem 1.1 of Paper 13 states RH **unconditionally**:

> "**Theorem (Riemann Hypothesis).** All non-trivial zeros of
> the Riemann zeta function lie on Re(s) = 1/2."

This does not say "conditional on CCM". It claims to prove RH.

The proof that follows, however, uses CCM as an external input
that is not re-derived. In effect, the "proof" is:

  CCM (Layer 1) + ITPFI + Estimates + Teschl-Bögli + Hurwitz = RH.

If CCM is viewed as a published/established result, the final
statement is unconditional. If CCM is viewed as an unrefereed
preprint (its current status), the final statement is
**conditional on CCM being correct**.

## The honest framing

A correctly framed theorem statement would be:

> "**Theorem (RH, conditional on CCM 2025).** Assuming the
> results of Connes-Consani-Moscovici arXiv:2511.22755 (in
> particular Theorems 4.2 and 5.10, and Lemmas 7.2, 7.3), all
> non-trivial zeros of the Riemann zeta function lie on
> Re(s) = 1/2."

This is less dramatic but accurate. Paper 13 instead gives the
unconditional statement and acknowledges the dependence only in
the "honest accounting" section (13.6).

## Is this acceptable?

**For a conditional result**, the framing is fine as long as the
dependence is noted somewhere. Paper 13 does note it.

**For a claim to prove RH**, the framing is **not** fine. RH is
the specific unconditional statement "all non-trivial zeros have
Re(s) = 1/2". A proof of "RH assuming X" is a proof of a
different theorem — namely, "X → RH" — not of RH itself. Clay's
millennium rules (Section 4(d)) require the paper to answer the
specific questions in the official description, which is the
unconditional RH statement.

By stating Theorem 1.1 as unconditional, Paper 13 implicitly
claims to satisfy Clay's requirement. But the proof actually
delivered is only "CCM ⇒ RH", not RH. This is a **framing
overreach**.

## Paper 13's own Strategy 26 says the right thing

Strategy 26 (the post-fix state document) correctly identifies
this:

> "The Riemann Hypothesis has a structurally complete proof at
> 8/10 confidence. The proof is adversarially verified (7/10
> initial, fixed to 8/10). It uses our ITPFI (proved), CCM's
> operators (preprint), Boegli's theorem (published), and
> Hurwitz (classical)."

The "8/10 confidence" framing is honest and appropriate. The
Theorem 1.1 statement in the preprint itself, however, is
**stronger than 8/10** — it claims RH outright.

This inconsistency between the theorem statement and the honest
accounting is a red flag. A refereeable version should either:

(a) Restate Theorem 1.1 as conditional on CCM, explicitly, OR

(b) Independently establish the CCM ingredients (which Paper 13
    does not attempt).

## Verdict on this subpoint

**The proof is conditional on CCM, but is framed as
unconditional.** Paper 13's theorem statement and abstract over-
claim. The honest-accounting section in Chapter 13 corrects the
framing, but the headline claim is unsupportable by the paper
alone.

**Required fix:** restate Theorem 1.1 as "Assuming CCM 2025,
...". If the authors wish to claim unconditional RH, they must
re-derive the relevant CCM results from scratch or cite them
from a refereed source (which does not exist).

This is a substantive issue, not a cosmetic one. It affects
the Clay-millennium evaluation directly.
