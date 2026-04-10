# Research 49 -- Lead O: Direct Limit Operator + Cartwright

*Date: 2026-04-09. Roles: DEVELOPMENT then ADVERSARIAL.*

---

## PART A: Development

### 1. The proposal

Define QW^inf directly as a compact self-adjoint operator on a fixed
L^2([L^{-1}, L]), with kernel given by the full Weil explicit formula
(all primes). Apply Cartwright to its eigenfunctions -> simplicity.
Then use simplicity to control finite-N approximations via Kato.

### 2. The kernel of QW^inf

The CCM Weil quadratic form decomposes as (Research 20, CCM eq 5.2):

    T = tau^{(0,2)} + tau^{(R)} + sum_p tau^{(p)}

As a continuous integral operator on L^2([L^{-1}, L]):

    K_inf(x,y) = K_arch(x,y) + sum_{all p} (log p / sqrt(p)) cos((x-y) log p)

K_arch involves digamma/Riemann-Siegel theta terms that saturate
as L -> inf (Research 20: rho(x) ~ exp(-x/2)).

### 3. Is K_inf in L^2([L^{-1}, L]^2)? -- CRITICAL FAILURE

The HS norm requires int int |K_inf(x,y)|^2 dx dy < inf. The prime
sum contributes ~ sum_p (log p)^2 / p * C(L). By PNT and partial
summation, sum_{p <= X} (log p)^2 / p ~ (log X)^2 / 2 -> inf.

THE SUM DIVERGES. K_inf is NOT in L^2. QW^inf is not Hilbert-Schmidt,
may not be compact. The spectral theorem for compact operators fails.

### 4. The CCM limit structure

CCM take L -> inf and N -> inf together (L^2 = P_N). Their operators
D(L,N) live on GROWING spaces L^2([L^{-1}, L]). There is no single
"QW^inf on a fixed L^2" with all primes -- the active prime count
(p <= L^2) grows with L. ITPFI proves STATE convergence only
(Research 14); operator norm convergence fails (Research 15: alpha
= 1/2 exactly, sum of perturbation norms diverges by Mertens).

---

## PART B: Adversarial

### 5. Attack: K_inf diverges -- QW^inf does not exist

The kernel sum sum_p (log p / sqrt(p)) cos((x-y) log p) diverges
absolutely for each (x,y). By PNT: sum_{p <= X} log p / sqrt(p)
~ 2 sqrt(X) / log X -> inf. Not borderline; blows up like sqrt(X).
QW^inf as an integral operator on a fixed space does not exist.
Lead O's Step 1 fails immediately.

### 6. Attack: Kato perturbation theory

Even granting existence, Kato needs operator norm convergence
QW^N -> QW^inf. Each rank-one perturbation has norm:

    ||alpha_p v_p v_p^T|| ~ (log p / sqrt(p)) * (L - L^{-1})

The Cauchy condition requires sum_{p > P} log(p)/sqrt(p) -> 0.
This sum DIVERGES. Research 15 confirmed: alpha = 1/2 exactly,
Kato-Rellich does not apply. No conditional convergence either
(Research 15 Sec 5.3: P(1/2 + it) diverges, no phase cancellation).

### 7. What DOES converge?

- State convergence (ITPFI): weak-* topology. Proved.
- Spectral convergence numerically: CCM's 10^{-55} with 6 primes.
- Strong resolvent convergence: OPEN. Would suffice but unproved.

None give QW^inf as a bounded operator on a fixed space.

---

## PART C: Can conditional convergence save it?

### 8. The Weil explicit formula has cancellation

The explicit formula involves h-hat(log p), not bare cosines:

    sum_gamma h(gamma) = ... + sum_p (log p / sqrt(p)) sum_m h-hat(m log p) / p^{m/2}

For h Schwartz, h-hat decays rapidly and the sum converges. But
for the KERNEL (h ~ delta function), h-hat does NOT decay. The
explicit formula as a kernel identity is distributional, not pointwise.

### 9. Distributional interpretation

K_inf might exist as a DISTRIBUTION, making QW^inf densely defined
but possibly unbounded. Unbounded SA operators can have continuous
spectrum; the compactness-based Cartwright argument does not apply.

Alternatively: define QW^inf via its QUADRATIC FORM (the Weil
positivity condition). The form sum_p (log p / sqrt(p)) |h-hat(log p)|^2
converges for Schwartz h (rapid decay of h-hat). But forms do not
have eigenfunctions in the operator sense.

### 10. The fundamental tension

The Cartwright argument REQUIRES:
- A compact operator (discrete eigenfunctions)
- Eigenfunctions in L^2 of a bounded interval (Paley-Wiener)
- All primes present (DPTZ simplicity)

Including all primes destroys compactness (divergent kernel).
Restricting to finitely many primes preserves compactness but
gives only finitely many overlap conditions from DPTZ.

This is the Step 10 wall in a new guise: the Cartwright mechanism
works at every finite stage but the limit operator does not exist
in the required sense.

---

## HONEST VERDICT

**Lead O is KILLED. Confidence: 9/10.**

The kernel sum diverges absolutely AND conditionally (Research 15,
Sec 5.3: P(1/2+it) diverges). QW^inf does not exist as a bounded
operator on any fixed L^2 space.

Strategy 28 Sec 3 asserts "the full Weil kernel is L^2" -- FALSE.
The HS norm diverges by Mertens/PNT. The claim "existence comes
from ITPFI, not from limits" is also wrong: ITPFI gives state
convergence, not operator existence on a fixed Hilbert space.

**What survives:** The Cartwright mechanism + DPTZ gives simplicity
at each finite N (Steps 1-7 of the chain). This is genuine math.
What fails is pushing to N = inf via a direct limit operator.

**What could revive a variant:** If QW^inf could be defined as a
closed (possibly unbounded) self-adjoint operator via the quadratic
form associated to Weil positivity, AND this operator has compact
resolvent, then the Cartwright argument might apply to eigenfunctions
of the resolvent. This would require: (a) the Weil form defines a
closed sectorial form, (b) the associated operator has discrete
spectrum, (c) eigenfunctions remain compactly supported. All three
are unproved and (c) is likely false for an unbounded operator on
L^2(R) -- eigenfunctions of unbounded operators are generally not
compactly supported.

**The Step 10 wall remains.** A fundamentally new ingredient is
needed beyond direct-limit Cartwright.
