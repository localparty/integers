# Paper 13 Cascade Note

*Amendments required in other papers as a consequence of the Paper 13
independent review.*

*Date: 2026-04-09*

---

## 1. Paper 23 (CBB system definition)

**Amendment required:** Axiom 1 should include an explicit discussion
of the gap between Meyer 2005's distributional spectral realisation and
the operator-theoretic statement (compact resolvent, genuine ONB). This
gap is currently implicit. Paper 23 should either:

(a) Prove the compactification step (distributional eigenstates -->
genuine eigenvectors of an operator with compact resolvent), OR

(b) State it as a structural axiom with explicit acknowledgment that
the distributional-to-operator promotion is assumed.

**Priority:** HIGH. This directly affects whether Paper 13 is
conditional or unconditional.

## 2. Paper 24 (Bridge family)

**Amendment required:** Elevate Lemmas 3.4 (k=4) and 3.5 (k=6) from
"structural" to "formal lemma" status. The proofs as written in Paper 13
Sections 3.4 and 3.5 appear complete:

- k=4: Arithmetic side computed (ord_13(3)=3, k=4, Hasse invariant 1/4),
  operator side cited (Jones 1983, Ocneanu 1985), coboundary check
  exhaustive on all 64 triples. This IS a proof.

- k=6: Arithmetic side computed (ord_19(7)=3, k=6, Hasse invariant 1/6),
  operator side cited (Ocneanu 1985), coboundary check exhaustive on
  all 216 triples. This IS a proof.

Paper 24 should declare these as formal lemmas, matching the status
of k=3 from research/162.

**Priority:** HIGH. The Gelfond-Schneider argument needs two proved
bridges. With k=3 and k=4 both proved, the argument is complete.

## 3. Anchor document (27-anchor-document.md)

**Amendment required:** Update the bridge table entry for k=4 and k=6
to reflect formal lemma status (once Paper 24 elevates them). Currently
the anchor says "Proved formally at k=3 (research/162, lemma)." It
should say "Proved formally at k=3,4,6 (research/162, 263, lemmas)."

**Priority:** MEDIUM. Depends on Paper 24 amendment.

## 4. Paper 13 itself

**Self-amendments identified by this review:**

(a) **Theorem 1.1 framing:** Consider restating as a conditional
theorem ("Assuming the CBB axioms...") or splitting into Theorem A
(conditional: axioms --> RH) and Theorem B (claim: axioms hold).

(b) **Section 6.3 presentation:** Demote the "two independently
specified transcendental numbers" argument to a heuristic remark.
Promote the Remark after Proposition 6.1 (the elementary
Gelfond-Schneider argument: LHS rational, RHS transcendental) to
the main proof line.

(c) **Section 8 (Nelson):** Add a remark that the direct spectral
argument (deficiency indices (0,0)) also suffices, independent of
Nelson. Keep Nelson for robustness.

(d) **Sections 3.4, 3.5:** Explicitly declare Lemmas 3.4 and 3.5 as
proved (formal lemma grade). The proofs are on the page. The
adversarial residual (Section 11.6, Residual A) should be updated
to reflect that the proofs written in Sections 3.4-3.5, when combined
with the published references (Jones 1983, Ocneanu 1985), constitute
complete proofs.

**Priority:** HIGH for (a) and (d). MEDIUM for (b) and (c).

## 5. Paper 25 (Hilbert 12 programme)

**No amendment required.** Paper 25 is downstream of Paper 13 and
can reference the conditional status without modification.

## 6. Papers 12, 14 (Deductions, Predictions)

**Minor amendment:** If Paper 13 is presented as conditional, then
any statement in Papers 12 or 14 that says "RH is proved" should be
softened to "RH is proved conditional on the CBB axioms" or "RH follows
from the CBB system."

**Priority:** LOW. Depends on the framing decision for Theorem 1.1.

---

## Summary of cascade actions

| Target | Amendment | Priority | Blocking? |
|:-------|:----------|:---------|:----------|
| Paper 23 | Axiom 1 gap discussion | HIGH | Yes (for unconditional) |
| Paper 24 | Elevate k=4,6 to lemma | HIGH | Yes (for proof completeness) |
| Anchor doc | Update bridge table | MEDIUM | No |
| Paper 13 | Reframe Theorem 1.1 | HIGH | No (internal) |
| Paper 13 | Promote elementary G-S argument | MEDIUM | No |
| Paper 13 | Add direct SA remark | MEDIUM | No |
| Paper 13 | Declare Lemmas 3.4, 3.5 proved | HIGH | Yes |
| Papers 12, 14 | Soften RH language | LOW | No |

---

*End of cascade note.*
