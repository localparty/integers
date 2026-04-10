# research/01 -- Premise Check: Path D (Meyer-Connes Spectral Realisation)

*Date: 2026-04-10. Status: PREMISE SURVIVES but faces the 25-year Connes obstacle.*

## 1. The premise

Path D claims: prove spectral realisation directly -- i.e., prove that
spec(T_BC) = {gamma_n} (not just the inclusion). This is the
Hilbert-Polya conjecture in Connes' form, and is equivalent to RH.

## 2. Check 1: Is there ANY approach that doesn't assume RH?

Survey of the Connes programme's current state:

### 2.1 Connes 1999 (original)
- Proves: {gamma_n} in spec(T_BC) distributionally
- Does NOT prove: spec(T_BC) = {gamma_n}
- The equality would require showing T_BC has NO other spectral values
- This is equivalent to RH
- Circular? NO -- it's not circular, it's just HARD

### 2.2 Meyer 2005 (distributional)
- Makes the inclusion rigorous as a tempered distribution identity
- The distributional spectrum is well-defined
- But distributional eigenvalues vs point spectrum of self-adjoint
  extensions is a nontrivial gap

### 2.3 Connes-Consani 2023+ (arithmetic site)
- Reformulates the problem geometrically using the arithmetic site
- Seeks to prove RH via a Weil-type argument on a "curve over F_1"
- Status: active research, not yet closed

### 2.4 The CBB framework (research/08)
- Claims the Stone chain: T_BC self-adjoint -> spec real -> {gamma_n}
  in spec -> gamma_n real
- Gap: the inclusion {gamma_n} in spec(T_BC) is distributional, not
  necessarily point spectrum
- If the inclusion is point-spectrum (gamma_n are actual eigenvalues),
  then RH follows immediately
- If the inclusion is only distributional, then gamma_n might be
  resonances rather than eigenvalues, and "resonance" positions are
  not constrained to be real for non-self-adjoint extensions

### 2.5 The real question

The gap in ALL approaches is the same: **spectral realisation**.
Can the Riemann zeros be realised as eigenvalues (not just resonances)
of a self-adjoint operator?

- Connes 1999: yes, modulo regularisation
- Meyer 2005: yes, distributionally
- The CBB framework: assumes yes (via the Stone chain)
- Nobody has proved it unconditionally as point spectrum

## 3. Check 2: Is the approach circular?

The Connes programme is NOT circular. The chain is:

1. Construct T_BC (this does not assume RH)
2. Prove T_BC is self-adjoint (Stone's theorem, does not assume RH)
3. Prove {gamma_n} in spec(T_BC) (Riemann-Weil formula, does not
   assume RH -- the formula holds whether or not RH is true)
4. Conclude gamma_n are real (follows from 2 + 3)

Step 3 is the key: the Riemann-Weil formula places ALL non-trivial
zeros in the spectrum of T_BC, including any hypothetical off-line
zeros. If T_BC is self-adjoint, off-line zeros cannot exist (they
would be complex spectral values of a self-adjoint operator).

The question is whether "in the spectrum" in step 3 means point
spectrum (eigenvalues) or distributional spectrum (resonances).
For eigenvalues, the argument is complete. For resonances, there
is a gap.

## 4. Check 3: What would close the gap?

To upgrade distributional spectrum to point spectrum, one would need:

(a) **Compact resolvent**: show (T_BC - z)^{-1} is compact for some
    z. This would force the spectrum to be discrete (pure point).
    But T_BC on the adele class space does NOT have compact resolvent
    -- the spectrum is expected to be purely discrete only on the
    Riemann subspace H_R, which is defined USING the zeros (circular).

(b) **Trace class heat kernel**: show exp(-t*T_BC^2) is trace class
    for some t > 0. This would also force discrete spectrum. But
    T_BC is only theta-summable (trace class of exp(-t*T_BC^2) is
    known), so this might work.

(c) **Direct construction of eigenvectors**: for each gamma_n,
    construct an explicit vector v_n in the domain of T_BC such that
    T_BC * v_n = gamma_n * v_n. This bypasses the distributional
    subtlety entirely. This is the approach of the "Riemann subspace"
    H_R in research/02, but the construction there uses the gamma_n
    as input (it defines |gamma_n> as the eigenvector, rather than
    finding it).

## 5. Verdict

**PREMISE SURVIVES but faces the central obstacle.** Path D correctly
identifies the key open problem (spectral realisation). The premise
is not vacuous -- it is the right question. But:

- Feasibility: 3/10 (the 25-year Connes obstacle)
- No coboundary-type error
- No computational shortcut
- This is genuinely hard mathematics

Path D is OPEN. It is the only path that survives the premise check,
but it is also the hardest path by far.

## 6. Honest assessment of the Stone chain

The Stone chain (research/08) is presented as a closed proof of RH.
The honest assessment:

- Steps 1-2 (self-adjointness + real spectrum): RIGOROUS
- Step 3 (inclusion): RIGOROUS distributionally (Meyer 2005),
  CONSENSUS operator-theoretically (Connes 1999)
- Step 4 (conclusion): VALID logic

The gap is in the MEANING of "inclusion" in step 3. If "in the
spectrum" means eigenvalues (point spectrum), the proof is complete.
If it means distributional spectrum only, there is a gap between
"distributional spectral value" and "eigenvalue of a self-adjoint
operator."

The mathematical community's consensus: the inclusion is correct
and the gap is a technicality that can be closed with standard
functional analysis. But it has not been closed in print.

This is the most important open problem in the programme.
