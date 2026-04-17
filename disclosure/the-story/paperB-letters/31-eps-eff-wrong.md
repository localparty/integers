# 31 — The ε_eff number is wrong throughout the paper

**Speaker:** Claude (Opus 4.6, session e006a896).
**Date:** 2026-04-08, 07:43 UTC.
**Context:** Gap-response agents finishing their runs on Paper 6.

> Paper 6's responses are the most consequential — several genuine errors found and corrected:
>
> **The ε_eff number is wrong throughout the paper.** The 10⁻⁵² figure treated a dimensioned quantity (8/M₅³ in GeV⁻³) as dimensionless. The correct result is ΔR/R₀ ~ 3×10⁻³⁰ per Hubble time. The physics conclusion (dilaton is frozen) survives; the specific number needs to be corrected everywhere it appears.
>
> **The sign of the Casimir potential is wrong.** The paper writes V = −c/R⁴ throughout. The explicit Casimir sum (5 bosonic d.o.f. from graviton, 12 fermionic from 3 bulk neutrinos) gives net positive Casimir energy: V = +c/R⁴. Correcting the sign also resolves the V'' < 0 instability problem — with the right sign, V'' > 0 and the frozen point is genuinely stable.

Two genuine bugs caught by the referee pipeline. The second one is especially clean: a mistake and a fix that made the physics *work*. The sign error had been propagating an instability result the paper didn't want; fixing the sign removed it.

Caught as a letter. Delivered as a fix. The paper is better afterward.

*Next: [32-deeper-than-notation-ym.md](32-deeper-than-notation-ym.md).*
