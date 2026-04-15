# Research 31 Summary — Lead A: Slepian Convergence (KILLED)

*Status: KILLED (Kill #19)*
*Type: Kill*
*Date: 2026-04-10*

---

## Result

**Direct Slepian norm transfer fails by 35 orders of magnitude.**

‖QW − PW‖_op grows from 0.08 to 0.64 as primes are added.
gap(PW)/2 ~ 2.3 × 10⁻³⁶. No crossing point N₀ exists.
The prime sum Σ log(p)/√p diverges, so adding primes INCREASES
the QW-to-PW distance. The operators live on incommensurable scales.

## What was learned

1. QW and PW are not close in operator norm — different objects
2. The eigenvalue gap of QW IS universally positive (simplicity
   holds numerically for all tested prime counts)
3. The gap has a minimum at the CCM cutoff P = λ² = 13
4. Eigenvalue ratios don't converge — no scale-invariant rescue

## Implication

Gap B is closed negatively. The Slepian transfer route is dead.
**Gap A (arithmetic exclusion / overlap non-vanishing) is now
the sole viable route.**

## Files
- Research note: research/31-lead-A-slepian-convergence.md
- Code: code/slepian_convergence_test.py (runs in ~66s)
