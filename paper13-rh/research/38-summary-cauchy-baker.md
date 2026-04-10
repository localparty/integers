# Research 38 Summary — Lead I: Cauchy + Baker Induction

*Status: COMPLETED (scoping note)*
*Type: Partial lead (base case works, induction blocked)*
*Feasibility: 4/10*
*Date: 2026-04-10*

---

## Result

Base case (K=0): Lindemann-Weierstrass proves SPO_0 for Cauchy
eigenvectors (explicit formula, all-nonzero components, algebraic
coefficients × algebraically independent exponentials).

Inductive step (K≥1): eigenvectors become transcendental after
adding primes. Baker controls linear forms but SPO involves
sums of products → algebraic independence → needs Schanuel
(unproved).

## The sign-control partial rescue

For the LEADING eigenvector (k=1): all components positive
(Gantmacher-Krein) + cos(x_i·log p) > 0 for small x_i → sum
of positive terms → nonzero. Works for k=1 at all K.

For general k: sign patterns oscillate. Sign tracking through
the secular equation induction is intractable.

## Files
- Research note: research/38-lead-I-cauchy-baker-induction.md
