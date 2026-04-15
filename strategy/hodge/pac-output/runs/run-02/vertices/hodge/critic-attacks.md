# Hodge Compliance Audit — Critic Attacks (run-02)

*Critic pass on author's 48-cell draft. Dissents proposed with rationale. Arbiter resolves in `arbiter-decisions.md`.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Summary

- Author verdicts reviewed: 48
- Critic dissents raised: **10**
- Cells left unchallenged: 38

## Dissent catalog

### D1. L5 Req 3 — author P, critic Pa

**Author**: P — "CP² × S² has no AH torsion; claim rational-consistent."
**Critic**: Pa — L5 is a specific known instance; verdict P over-claims requirement-wide coverage. The requirement is "RATIONAL not integral + AH obstruction acknowledged"; L5 does not acknowledge AH generally, it just happens to have no torsion. The AH obstruction is a PROGRAMME-LEVEL disclosure, not a per-link one. Verdict should be Pa with bypass→ADR-3.
**Recommendation**: downgrade to Pa.

### D2. L6 Req 1 — author Pa, critic S

**Author**: Pa — "Hitchin moduli smooth quasi-projective; scope compatible after stability restriction."
**Critic**: S — Simpson's nonabelian Hodge correspondence works on Kähler, not exclusively projective; Hitchin moduli is a moduli SPACE, not a smooth projective variety X on which the Hodge conjecture is stated. Route B's Hodge structures live on Hitchin space; mapping back to Hodge on an arbitrary smooth projective X requires L7 composition. L6 does not itself address scope of original X. Verdict should be S → ADR-1 (at L8).
**Recommendation**: downgrade to S.

### D3. L6 Req 2 — author Pa, critic Pa (confirm with caveat)

**Author**: Pa — "Hitchin moduli carries natural Hodge structure (Simpson)."
**Critic**: Pa confirmed, BUT — the Simpson Hodge structure on Hitchin moduli is nonabelian; the Clay Hodge-decomposition requirement concerns the ABELIAN (classical) Hodge structure on a fixed smooth projective X. Route B produces Hodge structures via the Hitchin fibration; the connection to classical Hodge on X is via derived equivalence / spectral decomposition. Keep Pa but sharpen citation.
**Recommendation**: confirm Pa; strengthen citation to include GR24 §5 (spectral decomposition linking Hitchin to classical Hodge).

### D4. L7 Req 6 — author O, critic Pa

**Author**: O — "W3 covers all (p, N) within BC-motivated; generic OPEN at L8."
**Critic**: Pa — once W3 closes (L^2-25), the BC-motivated class covers all (p, N) in that subclass; the cell addresses the requirement for the slice. Verdict should be Pa (known for slice, open-generic-at-L8 is W2 not W3).
**Recommendation**: downgrade O to Pa (W3 does not carry the Req 6 wall; W2 does).

### D5. L4 Req 4 — author Pa, critic Pa (confirm, STRENGTHEN)

**Author**: Pa — "std conj D concerns num vs hom equivalence; ab-var-powers PROVED."
**Critic**: confirmed Pa. FMS24 is explicit about cl(Z) (algebraic-cycle class = numerical class on ab-var-powers). Citation is sound.
**Recommendation**: keep Pa; strengthen with explicit "cl(Z) via Chern of ab-var universal bundles" citation.

### D6. L1 Req 3 — author S, critic Pa

**Author**: S — "H^{p,p} = ℚ vacuous at weight 0."
**Critic**: Pa — L1 Artin motives are 0-dimensional so the AH obstruction is vacuous BY DIMENSION; this vacuous-compliance is nonetheless addressing the requirement (trivially). Verdict should be Pa (not S) — the requirement is satisfied at this layer, trivially but validly.
**Recommendation**: upgrade S to Pa with "vacuous at weight 0; ℚ-structure automatic" annotation.

### D7. L2 Req 3 — author Pa, critic Pa (confirm)

**Author**: Pa — "Tannakian category is ℚ-linear."
**Critic**: confirmed. Deligne-Milne Tannakian is explicitly ℚ-linear.
**Recommendation**: keep Pa.

### D8. L3 Req 3 — author Pa, critic Pa (confirm)

**Author**: Pa — "Motivic Galois acts on ℚ-structure."
**Critic**: confirmed. G_mot acts on ℚ de Rham; AH obstruction respected structurally.
**Recommendation**: keep Pa.

### D9. L8 Req 6 — author O, critic O (confirm, STRENGTHEN)

**Author**: O — "L8 IS all-codim-all-dim functoriality; W2 wall."
**Critic**: confirmed O. STRENGTHEN: bypass includes FMS24 (ab-var-powers all (p, N) PROVED) + Kodaira-Spencer Del[7] (p=1 all N PROVED) + restriction to BC-motivated for the rest.
**Recommendation**: keep O; strengthen bypass-route citation.

### D10. L1 Req 1 — author Pa, critic S

**Author**: Pa — "Artin motives come from étale covers; 0-dim projective /ℂ after base change."
**Critic**: S — L1 is about ENCODING Galois data; the scope requirement (projective non-singular /ℂ) is framework-level, not per-link. L1 doesn't ensure scope for the rest of the chain. Verdict should be S → ADR-1.
**Recommendation**: downgrade to S.

---

## Critic suggestions beyond dissents

### Suggestion S1. Separate Req 4 at L3

L3 has S for Req 4 (cl(Z)/Chern). Since L3 is structural (motivic Galois on de Rham), it could be sharpened: motivic Galois action WOULD transport algebraic-cycle classes if W1 closes. Suggest: Pa-conditional-on-W1 annotation. But keep S to avoid over-reach (conditional verdicts weaken the §5d story).

### Suggestion S2. Add per-column §5d check

Every Deligne requirement must have ≥ 1 non-SILENT cell. Author's pre-critic counts show:
- Req 1: 7 non-S cells ✓
- Req 2: 6 non-S cells ✓
- Req 3: 7 non-S cells ✓
- Req 4: 5 non-S cells ✓
- Req 5: 5 non-S cells ✓
- Req 6: 5 non-S cells ✓

All 6 Deligne requirements are §5d-compliant. Arbiter should confirm after dissent resolutions do not remove all non-S from any column.

---

*End of critic-attacks.md. 10 dissents to resolve.*
