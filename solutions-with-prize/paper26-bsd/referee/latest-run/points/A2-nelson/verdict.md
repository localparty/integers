# Point A2 — Nelson self-adjointness over Q(i): Verdict

**Weight:** MEDIUM
**Location in preprint:** §3.7
**Overall rigor label:** **[THEOREM]**
**Overall verdict:** PASS

## Sub-question verdicts

- **(a) Entire analytic vectors.** [THEOREM] — The condition
  `cosh(t · log N(𝔞)) < ∞` is trivially satisfied for all t ∈ ℝ
  and all ideals 𝔞 of O_K, since log N(𝔞) is a finite real
  number. Identical to the Q case; proof inherits.

- **(b) Nelson's theorem hypotheses.** [THEOREM] — Reed-Simon
  X.39: a symmetric operator with a dense set of analytic vectors
  is essentially self-adjoint. The paper verifies density via the
  fact that Hecke operators {μ_𝔞} generate A_{BC,K}.

- **(c) The spectral consequence.** [THEOREM] — Essential self-
  adjointness implies spec(T̄_{BC,K}) ⊂ ℝ. This is a NECESSARY
  condition for the later arguments (which need real eigenvalues)
  but is **not sufficient** for the claimed point-spectrum
  identification with Riemann zeros.

## Combined finding

Nelson self-adjointness is a straightforward inheritance from
Paper 13's argument over Q, with N(𝔞) ≥ 1 ensuring the cosh
condition converges. The argument is standard and correctly
stated. The subtlety lies in what "spectrum" means: Nelson gives
a unique self-adjoint **closure** whose spectrum is real, but
having real spectrum does not guarantee any **specific**
spectrum. The claim that spec(T̄_{BC,K}) equals the imaginary
parts of ζ_K zeros is a separate, stronger claim addressed in
Point A3.

## Impact on the claimed result

**None at this level.** Nelson self-adjointness is a prerequisite
tool, not a source of novelty or risk. The real risk is Point A3
(Meyer-Nelson compatibility), not this step.

## Related concerns

The concern that "self-adjoint spectrum is real" is confused with
"the spectrum is the Riemann zeros" is addressed in Point A3.
Here, Nelson correctly gives the first; the second requires Point
A3's upgrade.
