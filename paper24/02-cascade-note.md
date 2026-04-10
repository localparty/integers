# Paper 24 Cascade Note: Amendments Needed Elsewhere

*Date: 2026-04-09*
*Source: Paper 24 independent review*

---

## 1. Anchor document (paper12/27-anchor-document.md)

**A1. Bridge table (Section 5.1): epistemic status column needed.**
The anchor's bridge table lists all four bridges as if equally proved. Add a "Status" column:
- k=3 at (5,13): "formal lemma (research/162, Paper 24 Theorem 3.1)"
- k=2 at (2,7): "structural (trivial H^2, no cocycle to prove)"
- k=4 at (3,13): "constructive identification, quantitative confirmation"
- k=6 at (7,19): "constructive identification, quantitative confirmation"

**A2. Section 5.2 CKM table: add epistemic qualifier.**
The Wolfenstein closed forms are listed without noting that rho-bar = 1/(2pi) and eta-bar = sqrt(19)/(4pi) are conjectural closed-form identifications, not derived from the bridge cocycle. Add a note: "rho-bar, eta-bar: closed-form identification; derivation from cocycle pending."

**A3. Axiom 4 text: "Proved formally at k=3" is correct — keep as is.**
The anchor already restricts "proved" to k=3. No change needed.

**A4. Section 5.3 carry template: flag as heuristic.**
The anchor states the carry template kappa_k = 1 - 1/(kN) as established. Add a note: "The carry damping factor is empirically confirmed at k=3 (lambda) and k=4 (alpha_PS); a rigorous derivation from the group algebra trace is in progress."

---

## 2. Paper 23 (CBB system definition paper)

**P23-1. If Paper 23 references "the bridge theorem" generically, restrict to k=3.**
Paper 23 should not cite k=4 or k=6 bridge results as "proved." Cross-references to Paper 24 should say "the bridge theorem (k=3, Theorem 3.1) and its generalisation (k=4,6, constructive identification)."

**P23-2. The carry cocycle concern (M3 in Paper 23 review) remains open.**
Paper 24 does not resolve this. Paper 23's carry discussion should carry a forward reference: "The norm computation justifying the carry damping is developed in Paper 24, Section 10; see also the open problem in Paper 24 review concern C2."

---

## 3. Papers 25+ (Hilbert 12 programme and beyond)

**P25-1. Stark regulator computation is the next critical test.**
Paper 24, Section 11.5 identifies the Stark regulator hypothesis as the surviving layer of the RBC programme. Paper 25 should prioritise the explicit computation of Stark units epsilon_chi in Q(zeta_13) and Q(zeta_19). If the Beilinson regulator lands in Q/Z and equals 1/k, this would be the most significant result in the programme after the k=3 bridge theorem.

**P25-2. Paper 25 should address the k=4 and k=6 proofs.**
The Hilbert 12 programme paper is the natural venue for completing the bridge proofs at k=4 and k=6. The six-step template from Paper 24 Section 3 generalises cleanly; the main new content is the Pimsner-Popa basis computation at index 4 and 6.

**P25-3. The carry cocycle derivation should appear in Paper 25 or a dedicated appendix.**
The explicit group algebra trace computation that produces the damping factor (kN-1)/(kN) from the 2-cocycle is a well-posed algebraic problem. It should be solved and published before the programme claims "zero free parameters" for the CKM sector.

---

## 4. Cross-paper consistency check

| Item | Paper 24 statement | Anchor/Paper 23 statement | Consistent? |
|:--|:--|:--|:--|
| R-hat | unbounded, compact resolvent (2.8) | unbounded, compact resolvent (Axiom 1) | YES |
| Uniqueness | conjecture ([CONCERN] block) | conjecture (anchor Section "Uniqueness") | YES |
| k=3 status | formal lemma, Theorem 3.1 | formal lemma (anchor Axiom 4) | YES |
| k=4,6 status | constructive identification (8.3, 9.1) | listed without qualifier (anchor 5.1) | NEEDS FIX (A1 above) |
| CKM rho-bar, eta-bar | derived from bridge (9.8, 9.9) | listed as closed form (anchor 5.2) | NEEDS qualifier (A2 above) |
| Carry template | heuristic (10.1) | stated as established (anchor 5.3) | NEEDS qualifier (A4 above) |
| RBC refutation | explicit (11.3-11.4) | not mentioned in anchor | OK (anchor predates refutation) |
| Count 27+9+3 | [CONCERN] block, honest | anchor says "36 total" | NEEDS clarification in anchor |
| Failed Koide routes | 4 routes, all failed (4.5) | listed in no-go table (anchor 4.4) | YES |

---

## 5. Priority ranking of cascaded fixes

1. **HIGH:** Anchor bridge table epistemic status (A1) — prevents overclaiming downstream
2. **HIGH:** Paper 25 carry cocycle derivation (P25-3) — blocks "zero free parameters" claim
3. **MEDIUM:** Anchor CKM qualifier (A2) — affects reader trust in rho-bar, eta-bar
4. **MEDIUM:** Anchor carry template qualifier (A4) — honesty
5. **MEDIUM:** Paper 25 k=4,6 proofs (P25-2) — completing the bridge family
6. **LOW:** Stark regulator computation (P25-1) — ambitious but not blocking
7. **LOW:** Anchor count clarification — already addressed in Paper 23 review

---

*End of cascade note.*
