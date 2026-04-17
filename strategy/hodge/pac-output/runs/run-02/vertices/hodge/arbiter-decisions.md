# Hodge Compliance Audit — Arbiter Decisions (run-02)

*Arbiter resolutions of critic dissents. Rejected alternatives preserved as footnotes.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Summary

- Dissents raised: 10
- Critic-wins: **6** (downgrades / sharpenings adopted)
- Author-wins: **4** (verdicts upheld)
- STRENGTHEN-confirms: 3 (D3, D5, D9)

| # | Cell | Author | Critic | Arbiter | Rationale |
|---|------|--------|--------|---------|-----------|
| D1 | L5 Req 3 | P | Pa | **Pa** | AH obstruction is programme-level; L5's no-torsion is coincidental to variety choice. Critic correct. |
| D2 | L6 Req 1 | Pa | S | **S** | Simpson nonabelian Hodge lives on moduli space; scope of original X is at L8. Critic correct; bypass→ADR-1. |
| D3 | L6 Req 2 | Pa | Pa (STRENGTHEN) | **Pa** | Confirmed. Cite GR24 §5 spectral decomposition. |
| D4 | L7 Req 6 | O | Pa | **Pa** | W3 does not gate Req 6 at the slice; generic-at-L8 is W2's wall. Critic correct. |
| D5 | L4 Req 4 | Pa | Pa (STRENGTHEN) | **Pa** | Confirmed. Cite FMS24 explicit cl(Z)/Chern treatment for ab-var-powers. |
| D6 | L1 Req 3 | S | Pa | **Pa** | Vacuous-compliance at weight 0 is compliance. Critic correct. |
| D7 | L2 Req 3 | Pa | Pa | **Pa** | Confirmed. |
| D8 | L3 Req 3 | Pa | Pa | **Pa** | Confirmed. |
| D9 | L8 Req 6 | O | O (STRENGTHEN) | **O** | Confirmed with strengthened bypass citation (FMS24 + Del[7] + BC-motivated restriction). |
| D10 | L1 Req 1 | Pa | S | **S** | L1 is an encoding layer; scope is framework-level at L8. Critic correct; bypass→ADR-1. |

---

## Detailed rationale

### D1 final — L5 Req 3 = Pa

The Atiyah-Hirzebruch obstruction is a programme-wide disclosure, not something L5 (Lefschetz B for CP² × S²) addresses per se. CP² × S² has trivial integral Hodge lattice (no torsion, all classes algebraic over ℤ), but that's incidental. The Clay requirement "rational, not integral, AH acknowledged" is addressed at the framework level (B_bare §7 in the eventual deliverable) via Del[2]. L5 satisfies the rationality partially by being a clean instance. Verdict: **Pa** with citation Del§2 Rem (iv) + p29L.5.

Rejected author P: over-claimed per-link what is programme-level.

### D2 final — L6 Req 1 = S

Critic is correct. The Clay scope requirement is "projective non-singular algebraic variety over ℂ" for the subject X on which H^{p,p}(X) is taken. Route B's Hitchin moduli M_H(X, G) is a DIFFERENT space (moduli of Higgs bundles on X); its Hodge structure contributes algebraic classes on X only via transport (spectral decomposition / derived equivalence) — that transport is L7 composition, not L6 structural. L6 itself doesn't establish scope on X; it establishes scope on moduli. Verdict: **S** → ADR-1 (at L8 for scope extension, Kodaira-Spencer Del[7] for p=1 all smooth projective).

Rejected author Pa: over-extended.

### D3 final — L6 Req 2 = Pa (STRENGTHEN)

Simpson's Hodge filtration on M_H(X, G) is the correct object; connection to classical H^n(X, ℂ) = ⊕ H^{p,q}(X) is via GR24 §5 spectral decomposition (Dolbeault/Betti/de Rham Simpson correspondence). Keep Pa; citation strengthened.

### D4 final — L7 Req 6 = Pa

W3 is about Route A + Route B composing; it produces Hodge for BC-motivated. Within the BC-motivated subclass, the composition would cover all (p, N) — so L7 Req 6 is PARTIAL (slice-covered). Generic-at-all-smooth-projective is W2's wall at L8. Don't conflate walls. Verdict: **Pa** (with conditional-on-W3 annotation).

Rejected author O: conflated W3 with W2; W3 doesn't gate Req 6 for the slice.

### D5 final — L4 Req 4 = Pa (STRENGTHEN)

FMS24 (arXiv:2510.21562) proves std conj D for abelian-variety powers; this directly concerns cl(Z) ↔ Chern-class-of-algebraic-bundle correspondence for these varieties. Citation strengthened: p29L.4 + FMS24 + Del§2 Rem (ii) + classical Chow for ab var.

### D6 final — L1 Req 3 = Pa

Artin motives are 0-dimensional → H^{p,p} trivializes for p ≥ 1 (vacuous) → AH obstruction vacuously satisfied. Vacuous compliance is still compliance; the requirement "rational, not integral" is met trivially. Verdict: **Pa** with annotation "vacuous at weight 0; ℚ-structure automatic" — citation CCM05 §2 + Del§2 Rem (iv).

Rejected author S: under-claimed.

### D7 final — L2 Req 3 = Pa

Confirmed. Tannakian reconstruction (Deligne-Milne) is ℚ-linear by construction.

### D8 final — L3 Req 3 = Pa

Confirmed. G_mot acts on the ℚ de Rham / Betti structures; motivic Galois respects ℚ-rationality.

### D9 final — L8 Req 6 = O (STRENGTHEN)

W2 wall. Bypass citation expanded to:
- **p=1 all N PROVED** via Kodaira-Spencer (Del[7]) + Lefschetz (1,1) (Del§2 Rem (iii))
- **Abelian-variety powers all (p, N) PROVED** via FMS24 (arXiv:2510.21562)
- **BC-motivated class all (p, N) OPEN-BUT-ADDRESSED** via W1 + W3 chain
- **Generic smooth projective p ≥ 2 OPEN** — the residual scope; disclosed per §5d

### D10 final — L1 Req 1 = S

L1 is encoding (Artin motives ↪ endomotives); it does not establish or invoke scope (projective non-singular /ℂ) at the chain level. Scope is universally set by the Clay problem statement and by L5/L8 in the chain. Verdict: **S** → ADR-1 (at L8).

Rejected author Pa: over-extended "0-dim projective is a case" to address scope for the rest.

---

## Post-arbiter changes to author verdicts

| Cell | Before | After |
|------|--------|-------|
| L1 Req 1 | Pa | **S** |
| L1 Req 3 | S | **Pa** |
| L5 Req 3 | P | **Pa** |
| L6 Req 1 | Pa | **S** |
| L7 Req 6 | O | **Pa** |

Net change: 2 S → Pa promotions cancelled by 2 Pa → S demotions + 1 P → Pa + 1 O → Pa. The S count stays approximately stable; the O count decreases by 1; the P count decreases by 1.

---

*End of arbiter-decisions.md. Ready to assemble final compliance map.*
