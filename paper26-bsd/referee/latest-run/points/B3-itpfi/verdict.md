# Point B3 — ITPFI factorization over Q(i): Verdict

**Weight:** LIGHT
**Location in preprint:** §5
**Overall rigor label:** **[LEMMA]** (standard operator-algebra
argument)
**Overall verdict:** PASS, modulo the MY3 twist concern

## Sub-question verdicts

- **(a) Factorization ω_1^K = ⊗_𝔭 ω_1^𝔭.** [LEMMA] — The
  three-step argument from Paper 13 transfers: Laca-Raeburn
  1996 (local KMS_1 uniqueness) + Bratteli-Robinson Proposition
  5.3.23 (tensor products of KMS states are KMS) + global KMS_1
  uniqueness (from Point A1). Standard.

- **(b) Gaussian prime decomposition.** [LEMMA] — The Borchers
  prime decomposition for A_{BC,K} uses prime ideals, not
  rational primes. Split primes contribute two prime ideals;
  inert primes one; ramified (p=2) one. The factorization handles
  all three cases. The paper's §5.2-5.3 briefly discusses this.

- **(c) Compatibility with spectral inclusion for ψ.** **[KEY
  LEMMA — OPEN]** — the ITPFI factorization of ω_1^K is well-
  defined, but whether the factored state's distributional
  spectral inclusion reaches L(s, ψ) depends on the same twist
  concern as Point A3 (MY3). The ITPFI factorization itself
  doesn't obstruct the twist, but the twist is not constructed.

## Combined finding

ITPFI factorization over Q(i) is a straightforward inheritance
from the Q case. The three-step argument (Laca-Raeburn + Bratteli-
Robinson + KMS uniqueness) transfers verbatim. The only concern
is the twist to L(s, ψ), which is inherited from Point A3 (MY3)
— the ITPFI factorization itself doesn't contribute new concerns.

## Impact on the claimed result

**Low severity at this point.** ITPFI is standard operator-
algebraic technology. The real concern lies upstream (A3 Meyer-
Nelson + twist). If A3 is closed, this point closes automatically.

## Action items

None at this point. The action is at Point A3 (construct the
twisted spectral realization for L(s, ψ) over K).
