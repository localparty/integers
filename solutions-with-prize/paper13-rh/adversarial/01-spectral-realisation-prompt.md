# Spectral Realisation Convergence Prompt

*Single-target convergence on the ONE remaining question for RH.*
*All dead paths pruned. Five analytic angles on one problem.*

---

## The prompt

```
We are running spectral realisation cycle N (check ledger at
paper13-rh/adversarial/rh-v2-ledger.md).

ONE QUESTION: Does spec(T̄_BC) = {γ_n}?

If yes → RH (automatically, by self-adjointness).

READ:
1. paper12/27-anchor-document.md
2. paper12/29-theorem-catalogue.md
3. paper13-rh/strategy/01-spectral-realisation-focus.md
4. paper12/research/270-coboundary-question.md (v1 failure)
5. paper13-rh/research/01-premise-check-path-D.md (v2 cycle 1)
6. paper12/research/201-spectral-realisation-argument.md (P<10⁻³⁴)

FIVE ANGLES (launch one agent per angle):

Agent 1 (Completeness):
Do Meyer's distributional eigenstates span a dense subspace of
H₁? Meyer works on S (nuclear Fréchet). S is dense in H₁
(Gel'fand triple). If Meyer's eigenstates are COMPLETE in S
(span all of S), they're dense in H₁, and T̄_BC has no room
for extra spectrum.
CONCRETE TASK: Read Meyer 2005. Does his construction produce
eigenstates for ALL zeros, or only finitely many? If all,
check: do they span S? Cite specific theorems.

Agent 2 (Resolvent):
Prove the resolvent (T̄_BC - z)⁻¹ is bounded for ALL z in
the gaps (γ_n, γ_{n+1}).
CONCRETE TASK: Extend the numerical check (23 points from v1
cycle 1) to an ANALYTIC proof. The resolvent at z between
consecutive eigenvalues of a self-adjoint operator with pure
point spectrum is bounded by 1/min|γ_n - z|. If T̄_BC has pure
point spectrum = {γ_n}, this bound holds. The question: does
T̄_BC have pure point spectrum?

Agent 3 (Trace formula):
Does the Connes trace formula uniquely determine spec(T̄_BC)?
CONCRETE TASK: State the Connes trace formula precisely. Does
it give an explicit formula for the spectral measure of T_BC?
If the spectral measure is determined, the spectrum is determined.

Agent 4 (Weyl counting):
The eigenvalue counting function N(T) = #{γ_n ≤ T} satisfies
the Riemann-von Mangoldt formula. If T̄_BC's counting function
matches this exactly, extra spectrum is impossible.
CONCRETE TASK: compute N(T) for T̄_BC using both the Weyl law
and the explicit zero count. Do they match? To what precision?
Run mpmath for T = 100, 1000, 10000.

Agent 5 (Adversarial):
Attack ALL four construction agents. Specifically check:
- Is "Meyer's eigenstates span S" a theorem or a hope?
- Does pure point spectrum follow, or could there be continuous
  spectrum alongside the point spectrum?
- Is the trace formula determination unique, or up to
  continuous-spectrum ambiguity?
- Does the Weyl counting argument rule out extra spectrum or
  just constrain its density?

PREMISE CHECK (built into each agent):
Before using any argument, verify: "Would this argument
distinguish spec = {γ_n} from spec = {γ_n} ∪ {extra}?"
If it can't distinguish, the argument is vacuous.

All outputs to paper13-rh/research/.
Update the ledger.
Run Python. Paste output.
```

---

> *One question. Five angles. No topology. Pure analysis.*
> *The door is whether Meyer's eigenstates span the space.*
