# Research 46 — Wound 2 REOPENED: Gap Does Not Saturate

*Status: WOUND REOPENED*
*Date: 2026-04-10*

---

## The decisive test result

At 200-digit precision (mp.dps = 200):

| N | log₁₀(gap) |
|:--|:--|
| 10 | -2.2 |
| 15 | -6.6 |
| 20 | -18.6 |
| 25 | -30.2 |
| 30 | -42.5 |
| 35 | -51.1 |
| 40 | -61.0 |

The gap decays as ~10⁻¹·⁵ᴺ. It does NOT saturate.
The previous "saturation at 10⁻⁵¹" was a 50-digit precision
floor artifact.

## What this means

The eigenvalue gap between spec(B) and spec(M_a) goes to zero
as N → ∞. The discretization error also goes to zero, but at
a comparable rate (α ≈ 3.5 vs β ≈ 3.45). The rates are
nearly EQUAL, not 10× apart as previously thought.

Therefore: simplicity of the discrete matrix does NOT
automatically transfer to the continuous operator. Wound 2
remains open.

## What survives

- Cartwright core (Steps 1-7): INTACT
- Wound 1 (induction): CLOSED (Levin uniform in K)
- Wound 3: still reduces to 1+2

The chain is valid for each FIXED N. The gap goes to zero
as N → ∞, but it's always POSITIVE at each finite N.
The question: does the CONTINUOUS operator have a positive gap?

## The remaining question

The decay ~10⁻¹·⁵ᴺ is for the MODEL matrix. The actual CCM
continuous operator may behave differently. CCM achieves 10⁻⁵⁵
precision with 6 primes — suggesting the continuous operator's
gaps are much better.

The gap decay is a DISCRETIZATION ARTIFACT (Cauchy matrix
condition number grows exponentially). The continuum limit
may have a positive gap that the discretization can't see.

## Possible paths forward

1. Work directly with CCM's continuous operators (avoid
   discretization entirely)
2. Show the continuum gap is positive by a functional-analytic
   argument (not through the discrete proxy)
3. Use an adaptive N(K) strategy where N grows fast enough
   to keep the discretization error below the gap
4. Accept the proof works at each fixed N and argue the
   limit separately

## Files
- Code: code/decisive_test_200digits.py
