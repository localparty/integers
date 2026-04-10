# research/01 -- Premise Check: Path C (Spectral Flow)

*Date: 2026-04-10. Status: PREMISE ILL-DEFINED (no valid operator family).*

## 1. The premise

Path C claims: the spectral flow SF({T_BC(delta)}) of a family of
operators parametrized by delta (the off-line shift) is integer-valued
and detects zero-crossings. If an off-line zero creates a crossing,
SF != 0, contradicting self-adjointness (which forces SF = 0 on a loop).

## 2. Check 1: Is the family {T_BC(delta)} well-defined?

The APS spectral flow requires a CONTINUOUS family of self-adjoint
operators {A(t)}_{t in [0,1]} on a fixed Hilbert space. The spectral
flow counts the net number of eigenvalue crossings through zero.

For Path C to work, we need:
- T_BC(0) = T_BC (the standard BC operator, self-adjoint)
- T_BC(delta) = "T_BC with an off-line zero at delta"
- The family must be continuous in delta
- Each T_BC(delta) must be self-adjoint

**Problem:** T_BC is self-adjoint (Stone's theorem). Its spectrum is
real. An off-line zero at 1/2 + delta + i*t would require a spectral
value at t - i*delta, which is COMPLEX. A self-adjoint operator cannot
have complex spectral values.

There is no self-adjoint deformation T_BC(delta) that "introduces"
an off-line zero. The premise requires a family of operators that
does not exist.

## 3. Check 2: Alternative formulation via beta-deformation

One could consider the family T_BC(beta) where beta varies from 1 to
some other value. At beta != 1, the KMS state changes and the modular
flow changes, so T_BC(beta) is a different operator. But:

- T_BC(beta) is self-adjoint for every beta (it is always a modular
  generator, and Stone's theorem applies).
- The spectrum of T_BC(beta) has no direct connection to off-line
  zeros of zeta. The Riemann-Weil explicit formula applies specifically
  at beta = 1 (the critical point of the BC phase transition).
- The spectral flow of {T_BC(beta)} counts eigenvalue crossings as
  beta varies, but this has no known connection to RH.

## 4. Check 3: Spectral flow of a non-self-adjoint deformation

If we allow non-self-adjoint operators (dropping the self-adjointness
requirement), we could define:
  T_BC(delta) = T_BC + delta * V
for some perturbation V that shifts spectral values off the real axis.

But:
- The APS spectral flow is defined only for self-adjoint families.
- For non-self-adjoint operators, eigenvalue crossings are not
  constrained to be integer-valued.
- The integer-valued nature of spectral flow (the key tool) is lost.

## 5. Verdict

**PREMISE IS ILL-DEFINED.** There is no valid operator family
{T_BC(delta)} that:
(a) is self-adjoint for all delta (required for spectral flow)
(b) has spectrum related to off-line zeros at delta != 0
(c) reduces to T_BC at delta = 0

The self-adjointness of T_BC (Stone's theorem) and the reality of
its spectrum (spectral theorem) are precisely the structural argument
of research/08 that ALREADY proves RH. Path C cannot add anything
beyond this because the "perturbation" it needs is incompatible with
self-adjointness.

Path C is BLOCKED: the operator family does not exist.

## 6. Coboundary lesson check

This is a different failure mode from v1: not a vacuous constraint but
an ill-defined setup. The spectral flow tool is valid mathematics, but
the object it would apply to (a self-adjoint family connecting T_BC to
"T_BC with off-line zeros") does not exist. This is more fundamental
than the coboundary gap.

## 7. Deeper issue

Paths A, B, and C all run into the same wall: T_BC is self-adjoint,
therefore its spectrum is real, therefore there are no off-line zeros.
This is the structural argument of research/08 (the Stone chain).
Any attempt to "detect off-line zeros" must grapple with the fact
that the operator formalism ALREADY excludes them.

The question is not "can we find a new invariant that detects off-line
zeros?" but rather "is the Stone chain a valid proof of RH?" The
Stone chain claims:
1. T_BC is self-adjoint (Stone's theorem)
2. spec(T_BC) is real (spectral theorem)  
3. {gamma_n} is in spec(T_BC) (Riemann-Weil explicit formula)
4. Therefore gamma_n are real (RH)

The gap in the Stone chain is NOT in steps 1-4 (which are all standard
theorems). The gap is in the IDENTIFICATION: does the Riemann-Weil
explicit formula genuinely place the gamma_n in the spectrum of T_BC?
The inclusion {gamma_n} subset spec(T_BC) is distributional (Meyer 2005),
and the distributional spectrum may not coincide with the point spectrum
of a self-adjoint extension.

This is the Meyer distributional subtlety (research/200 Section F.2,
Gap 4). It is the REAL open problem, not the premise checks of Paths
A/B/C.
