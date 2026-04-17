# 32 — Deeper than notation

**Speaker:** Claude (Opus 4.6, session 9605d38c).
**Date:** 2026-04-08, 02:18 UTC.
**Context:** Claude is running as adversarial math referee on the Yang-Mills proof; tracked a "notation inconsistency" into something deeper.

> I traced it. The inconsistency is **deeper than notation** — it's actually about which direction the recursion flows.
>
> So the proof has TWO halves with **opposite conventions** for $a_k$ and $\hat\Delta_k$:
> - §5.1.2 + §5.4.1 + §5.4.3: **coarsening** ($a_k$ grows, $\hat\Delta_k$ grows)
> - §5.4.6 + §5.7(b): **refining** ($a_k$ shrinks, $\hat\Delta_k$ shrinks)
>
> **The substantive issue:** which convention is the convergence sum *actually* relying on?
>
> If coarsening is right (§5.4.1), then $\hat\Delta_k^2 \sim 4^{+k}$ and $\sum_k k^{\gamma-2} \cdot 4^k$ **diverges**. The form-factor recursion explodes.
>
> If refining is right (§5.4.6/§5.7(b)), then $\hat\Delta_k^2 \sim 4^{-k}$ and the sum converges. But §5.1.2's "block-spin from fine to coarse" is then wrong, and §5.4.1's momentum-shell description doesn't make sense (the shell would be empty).
>
> **The convergence claim only works under refining.** So §5.4.6 + §5.7(b) are the "load-bearing" half, and §5.1.2 + §5.4.1 + §5.4.3 need to be flipped to match.

A genuine directional inconsistency caught inside the Yang-Mills proof — one that *would have made the convergence claim diverge* under the other reading. Claude follows a small notational hiccup into a load-bearing correction.

*The inconsistency is deeper than notation.* Four words that describe the posture. Not nitpicking — finding.

*Next: [33-camb-honest-bad-news.md](33-camb-honest-bad-news.md).*
