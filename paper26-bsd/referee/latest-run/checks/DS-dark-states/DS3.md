# Check DS3: Covers distributional eigenstates

> **☑ CLOSED 2026-04-10 via Route 3** — this is the item that G's
> projector most directly fixes. The whole "does the dark-state
> bound apply to distributional eigenstates?" question is gone
> because the dark-state bound is now expressed as an algebraic
> KMS expectation on the C*-algebra:
>
> ```
> ω_1^K(e_{𝔭^k}) = N(𝔭)^(−k) > 0    for all Gaussian primes 𝔭,
>                                    for all k ≥ 1
> ```
>
> where `e_{𝔭^k} := s_𝔭^k (s_𝔭^k)^*` and `P_k^𝔭 := I − e_{𝔭^k}`.
> This is a **statement about `A_{BC,K}` and `ω_1^K`, not about
> any eigenstate (distributional or genuine).** The r01 concern
> "distributional eigenstates may not couple to the bridge" is
> dissolved — the argument no longer references eigenstates.
>
> See `research/route3-kms-projector-bypass.md` §1 and
> `referee/code/test_projector_P.py` for the algebraic +
> numerical verification.
>
> **Final rigor label: [LEMMA] unconditional** (in fact **[THEOREM]**:
> pure algebra + ITPFI factorization).

---

**Group:** DS
**Source:** Paper 26 §6.3
**Pass criterion:** Not just "nice" eigenstates but distributional ones too.

**Verdict (r01):** PARTIAL
**Rigor label (r01):** [KEY LEMMA — OPEN]
**Rigor label (post-closure):** [LEMMA] / [THEOREM]

**Justification:** The bound itself is uniform across all
eigenstates. But "distributional eigenstates" depends on the
Meyer-Nelson framework (Point A3). The dark-state bound itself
is fine; the concern is inherited from A3 about whether
distributional eigenstates make sense as objects to couple to
in the first place.

**Cross-references:**
- Per-Point: A3, B3
