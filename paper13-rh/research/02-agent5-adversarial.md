# research/02 -- Agent 5: Adversarial Review

*Date: 2026-04-10. Spectral Realisation Cycle 2.*

## 1. Mission

Attack all four construction agents. Find gaps, circular reasoning,
and false claims.

## 2. Attack on Agent 1 (Completeness)

### 2.1 "Meyer produces eigenstates for ALL zeros"

**VERDICT: CORRECT but with caveat.**

Meyer's Theorem 4.1 (Duke Math. J. 127, 2005) does produce
distributional eigenstates for all non-trivial zeros. The
construction uses the Weil explicit formula, which sums over ALL
zeros. No truncation.

**Caveat:** Meyer's construction is distributional (in S'). The
eigenstates are tempered distributions, not Hilbert space vectors.
The phrase "eigenstate for every zero" is misleading if read as
"eigenvector in H_1." It means "generalised eigenfunction in the
rigged Hilbert space."

### 2.2 "Spanning S implies pure point spectrum"

**VERDICT: CIRCULAR.**

Agent 1 correctly identifies this circularity in Section 3.3.
The nuclear spectral theorem gives a complete set of generalised
eigenfunctions for ANY self-adjoint operator -- including ones
with continuous spectrum. The generalised eigenfunctions for
continuous spectrum are not in {phi_n}. So completeness of
{phi_n} is EQUIVALENT to pure point spectrum, not a proof of it.

### 2.3 What Agent 1 misses

Agent 1 does not address: could T_BC have continuous spectrum
of Lebesgue measure zero? (A singular continuous component.) The
Weyl counting argument constrains the density of extra POINT
spectrum, but singular continuous spectrum has no eigenvalues at
all -- it is spectrally diffuse.

**This is a genuine threat.** Singular continuous spectrum is
notoriously hard to rule out. The anti-fine-tuning argument
(research/201) does not address it because it only constrains
point eigenvalues, not continuous spectral components.

## 3. Attack on Agent 2 (Resolvent)

### 3.1 "Resolvent = zeta'/zeta identification"

**VERDICT: FORMAL, NOT RIGOROUS.**

Agent 2 correctly flags this. The identification requires:
1. Compact resolvent for T_BC (unproved)
2. Trace-class resolvent (follows from compact resolvent + Weyl
   asymptotics, but unproved)
3. Proper regularisation of the Hadamard product

Without (1), the "resolvent" may not even be compact, and the
"trace" may not be a trace in the functional-analytic sense.

### 3.2 "zeta(1/2+iz) nonzero => no extra spectrum"

**VERDICT: ONLY VALID for point spectrum.**

If zeta(1/2+iz) is nonzero at z = z_0, this means z_0 is not a
zero of zeta. Under the resolvent = zeta'/zeta identification,
the resolvent is bounded at z_0, so z_0 is not in the POINT
spectrum.

**BUT:** z_0 could still be in the CONTINUOUS spectrum. The
resolvent of an operator with continuous spectrum is bounded at
every individual point in the continuous spectrum (the spectrum
is not isolated). The resolvent only has poles at point spectrum
(eigenvalues). Continuous spectrum manifests as the resolvent
failing to be bounded uniformly on a set, not at individual
points.

**This is a critical gap in Agent 2's reasoning.** Checking that
the resolvent is bounded at individual test points does NOT rule
out continuous spectrum.

### 3.3 The compact resolvent bottleneck

Both Agent 1 and Agent 2 reduce to the same obstruction: compact
resolvent for T_BC. This is the single load-bearing unproved claim.

## 4. Attack on Agent 3 (Trace Formula)

### 4.1 "Trace formula determines spectral measure uniquely"

**VERDICT: CORRECT but misleading.**

The Stone-Weierstrass argument in Section 3.2 is valid. The trace
formula does uniquely determine the spectral measure. But:

(a) Knowing the spectral measure is equivalent to knowing the
    operator (up to unitary equivalence). So this is tautological:
    the trace formula determines T_BC, which of course determines
    spec(T_BC).

(b) The question is not whether the spectral measure is determined,
    but what it IS. The trace formula tells us the spectral measure
    equals something involving the primes. The question is whether
    that something is a pure point measure at {gamma_n}.

### 4.2 "Extracting the answer requires RH"

**VERDICT: CORRECT.**

Agent 3 correctly identifies the circularity in Section 3.4.
The trace formula is symmetric between the RH-true and RH-false
interpretations. It does not select one.

### 4.3 "The H_R construction is circular"

**VERDICT: PARTIALLY CORRECT.**

Connes' construction of H_R does use the zeros. But Connes is
aware of this and proposes an intrinsic construction via the
semi-local trace formula (Connes-Consani 2021+). Whether this
intrinsic construction works is the 25-year open problem.

Agent 3 is too hasty in declaring circularity. The correct
statement is: "The current construction is circular, but a
non-circular intrinsic construction is the goal of the Connes-
Consani programme."

## 5. Attack on Agent 4 (Weyl Counting)

### 5.1 "O(log T) extra eigenvalues could hide"

**VERDICT: CORRECT for point spectrum; does not address continuous
spectrum.**

The Weyl counting argument constrains the number of extra POINT
eigenvalues. It says nothing about continuous spectrum, which does
not contribute discrete eigenvalues. A continuous spectral
component of measure epsilon in [T, T+1] would not change the
eigenvalue count.

### 5.2 "Anti-fine-tuning makes extra eigenvalues impossible"

**VERDICT: VALID heuristic, not a proof.**

The P < 10^{-34} bound assumes each formula's constraint on
lambda_extra is independent and uniformly distributed. Neither
assumption is rigorous:
- Independence: the formulas share the same gamma_n, so they are
  NOT truly independent.
- Uniform distribution: the distribution of lambda_extra's
  contribution depends on the operator structure, not a uniform
  prior.

The anti-fine-tuning argument is compelling heuristics, not
mathematics.

### 5.3 The Weyl law for T_BC

**CRITICAL POINT:** Agent 4 assumes that T_BC satisfies a Weyl
law matching the Riemann-von Mangoldt formula. This is only true
if T_BC has discrete spectrum (otherwise the counting function is
undefined). So the Weyl counting argument PRESUPPOSES discrete
spectrum, which is what we are trying to prove.

## 6. The meta-attack: what ALL four agents miss

### 6.1 Singular continuous spectrum

None of the four agents addresses singular continuous spectrum.
This is the most dangerous gap. A self-adjoint operator can have:
- Pure point spectrum (eigenvalues)
- Absolutely continuous spectrum (Lebesgue-class)
- Singular continuous spectrum (Cantor-set-like)

The anti-fine-tuning argument constrains extra POINT spectrum.
The resolvent argument constrains POINT spectrum (poles of the
resolvent). The Weyl counting constrains POINT spectrum (counting
function). The trace formula determines the spectral measure but
does not directly decompose it.

**None of these tools directly addresses singular continuous
spectrum.** For a proof, one needs to rule out ALL three types of
extra spectrum.

### 6.2 The operator domain question

All four agents assume T_BC is self-adjoint on a well-defined
domain. But the domain of T_BC on the adele class space is not
the same as the domain on H_R. The self-adjoint extension might
depend on the choice of domain. Different self-adjoint extensions
can have different spectra.

The CBB framework assumes a SPECIFIC self-adjoint extension
(the one given by Nelson's analytic vector theorem). But Nelson's
theorem requires the GNS vectors to be analytic for T_BC, which
is nontrivial on the adele class space.

## 7. Summary of attacks

| Agent | Main claim | Attack | Severity |
|:------|:-----------|:-------|:---------|
| 1 | Meyer eigenstates complete | Circularity: completeness = pure point | FATAL |
| 2 | Resolvent = zeta'/zeta | Formal, requires compact resolvent | BLOCKING |
| 2 | No extra poles found | Doesn't address continuous spectrum | CRITICAL |
| 3 | Trace formula determines measure | Tautological; doesn't determine type | MODERATE |
| 3 | H_R construction circular | Partially; Connes-Consani may fix | MODERATE |
| 4 | Weyl error bounds extra eigenvalues | Presupposes discrete spectrum | BLOCKING |
| 4 | Anti-fine-tuning P < 10^{-34} | Heuristic, not proof | MODERATE |
| ALL | No one addresses singular continuous spectrum | Genuine gap | CRITICAL |

## 8. Verdict

**THE SINGLE OBSTRUCTION: COMPACT RESOLVENT.**

All five angles reduce to one question: does T_BC (on the
appropriate space) have compact resolvent? Equivalently: is the
spectrum purely discrete?

If YES: spectral realisation follows from Meyer's inclusion +
Weyl counting + resolvent analysis (the machinery is all in place).

If NO: continuous spectrum is possible, and none of the current
tools can rule it out.

The honest feasibility assessment for proving compact resolvent
from within the BC algebra: **3/10**. This is the 25-year Connes
obstacle. It has not yielded to 25 years of effort by Fields
medallists. The CBB framework has powerful numerical evidence
(P < 10^{-34}) but no new analytic tools for this specific
problem.

**Status: ALL ANGLES OPEN. Single bottleneck identified: compact
resolvent for T_BC.**
