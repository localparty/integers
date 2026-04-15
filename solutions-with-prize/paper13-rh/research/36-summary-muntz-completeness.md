# Research 36 Summary — Lead G: Müntz-Szász Completeness

*Status: COMPLETED*
*Type: Partial lead (collective 9/10, individual 2/10)*
*Date: 2026-04-10*

---

## Result

{cos(x·log p)} is complete on any interval (Beurling-Malliavin,
infinite density). No function avoids all primes simultaneously.
But completeness doesn't give INDIVIDUAL overlaps (SPO).

## Key computational finding

On long intervals (L ≥ 20), the Gram matrix of {v_p} is robustly
PD with condition number ~5. The system approaches a Riesz basis.
Riesz basis → quantitative lower bounds on all overlaps.

## The gap

Completeness gives "collective" non-avoidance. SPO needs
"individual." The bridge is the Riesz basis property: if the
system is a Riesz basis (not just complete), every projection
has a lower bound.

## Files
- Research note: research/36-lead-G-muntz-completeness.md
- Code: code/muntz_completeness_test.py
