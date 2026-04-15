# C2.01 — What "AE" Means

## Paper 13's usage

"AE simplicity" in Paper 13 refers to simplicity for **all λ
except possibly a discrete subset** S_N of the λ-parameter
interval (1, ∞). The exceptional set S_N depends on N and is
(in Paper 13's argument) at worst discrete, hence measure zero.

So "AE" in this context means:
- **discrete exceptional set**,
- at each fixed N,
- in the λ-parameter,
- with S_N depending on N.

## Is this the standard "almost everywhere" notion?

Standard Lebesgue-AE on a real interval (1, ∞) requires the
exceptional set to have Lebesgue measure zero. A discrete set is
automatically Lebesgue-negligible, so Paper 13's usage is
consistent with standard AE.

However, **discrete** is a stronger condition than **measure
zero**. Paper 13 establishes the discrete property via the
identity theorem (real-analytic zero sets are discrete).

## Is AE sufficient for the proof chain?

Paper 13 Section 12.5 argues yes:

> "The Bögli argument (Section 9) requires AE simplicity at ONE
> specific λ = λ_N for each N, with λ_N not in the exceptional
> set S_N. Since S_N is discrete for each N, such a choice
> always exists."

And the "universal choice" λ_N = √14 is supplied by the certified
computation for N = 1, ..., 20.

**Is it true that the chain only needs simplicity at one λ?**
This is a subtle claim. CCM Theorem 5.10 requires simplicity for
its conclusions (i)–(iii). If we want to apply it at one specific
λ, simplicity at that λ is needed. OK.

But the **limit** D_∞ is constructed by N → ∞ at **fixed λ**. If
Paper 13 chooses λ = √14 as the "universal choice", then the limit
is spec(D_∞) at λ = √14. The eigenvalues of D_∞ at this specific
λ must match {γ_n}. This is a specific limit, not a general
statement about "all λ".

For the Hurwitz argument to then conclude that the zeros of Ξ are
real, we need ξ̂_N at λ = √14 to converge to Ξ. But Ξ is a
λ-independent function — it is the Riemann Xi, a fixed entire
function. So the convergence ξ̂_N → Ξ at fixed λ is the statement.

This is consistent with the paper's implicit "fixed λ" reading
(see B3.05, C1.01 discussion).

## Verdict on this subpoint

**Pass.** "AE simplicity" in Paper 13's usage is discrete-
exceptional-set simplicity, which is stronger than Lebesgue-AE
and sufficient for the downstream needs. The argument requires
only simplicity at one specific λ, and the universal choice
λ = √14 (certified for N ≤ 20) makes this explicit.
