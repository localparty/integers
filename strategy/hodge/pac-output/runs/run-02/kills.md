# Hodge Compliance Audit — Kills (run-02)

*WEAKENINGs and rejections recorded during the audit. Claims that were proposed stronger than the chain supports — the arbiter downgraded them.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Summary

- **KILLS registered**: 3 WEAKENINGs + 2 author-upgrades
- All KILLS recorded; no KILL affects chain validity or §5d compliance

---

## WEAKENINGs (arbiter downgrades of author verdicts)

### KILL 1 — L1 Req 1: Pa → S

**Proposed**: Pa ("Artin motives come from finite étale covers → 0-dim projective /ℂ after base change; scope addressed").
**Arbiter**: S ("L1 is an encoding layer; the scope requirement (projective non-singular /ℂ) is framework-level, not per-link. L1 does not itself establish or invoke scope for the rest of the chain. Scope is universally set by the Clay problem statement and addressed at L5 (PROVED instance) + L8 (W2 scope-expansion).").
**Bypass**: ADR-1 → p29L.5, p29L.8/W2.
**Effect on chain validity**: none. Scope IS addressed in the chain; just not at L1.

### KILL 2 — L5 Req 3: P → Pa

**Proposed**: P ("CP² × S² has no AH torsion; claim rational-consistent; requirement PROVED at this link").
**Arbiter**: Pa ("The Atiyah-Hirzebruch obstruction is a programme-wide disclosure, not something L5 addresses per link. CP² × S² happens to have trivial integral Hodge lattice, but that's incidental to the variety choice, not a proof-of-compliance for the Req. The Req is satisfied at framework level (B_bare §7) via Del[2]; L5 is a PARTIAL contributor (provides an instance where rationality is automatic).").
**Bypass**: ADR-3 → framework-level discipline + Del§2 Rem (iv) + Del[2].
**Effect on chain validity**: none. Req 3 is now 8/8 = 100% non-SILENT (all Pa); strongest column.

### KILL 3 — L6 Req 1: Pa → S

**Proposed**: Pa ("Hitchin moduli M_H(X, G) is smooth quasi-projective; scope compatible after stability restriction").
**Arbiter**: S ("The Clay scope requirement is 'projective non-singular /ℂ' for the SUBJECT variety X on which H^{p,p}(X) is taken. Route B's Hitchin moduli M_H(X, G) is a DIFFERENT space (moduli of Higgs bundles on X). Its Hodge structure contributes to H^*(X) only via transport (spectral decomposition / derived equivalence at L7). L6 does not itself establish scope on X; it establishes scope on moduli. This is a category error in the author pass.").
**Bypass**: ADR-1 → p29L.5, p29L.8/W2.
**Effect on chain validity**: none. Route B still contributes Hodge structure (Pa on Req 2) and algebraic-cycle origin (Pa on Req 4); just not scope.

---

## Author-upgrades (arbiter upgrades of author verdicts)

### UPGRADE 1 — L1 Req 3: S → Pa

**Proposed**: S ("Artin motives are 0-dim so H^{p,p} = ℚ trivially for p ≥ 1").
**Arbiter**: Pa ("Vacuous-compliance at weight 0 IS compliance. The Deligne requirement 'rational, not integral' is trivially satisfied — Artin motives are ℚ-structures by construction (CCM05 §2, Deligne-Milne). Annotate 'vacuous at weight 0'.").
**Effect on chain validity**: net-positive. Req 3 column upgrades from 7/8 to 8/8 non-SILENT.

---

## STRENGTHEN-confirms (arbiter agrees with critic to sharpen citation)

These are not KILLS but improved citations:

- **L6 Req 2**: Pa → Pa (strengthen citation with GR24 §5 spectral decomposition)
- **L4 Req 4**: Pa → Pa (strengthen citation with FMS24 explicit cl(Z)/Chern for ab-var-powers)
- **L8 Req 6**: O → O (strengthen bypass citation: p=1 via Del[7] + ab-var-powers via FMS24 + BC-motivated via W1+W3 + residual OPEN)

---

## Rejected critic suggestions (not adopted)

### REJECTED 1 — Suggestion S1: L3 Req 4 conditional-Pa

**Critic suggestion**: upgrade L3 Req 4 from S to "Pa-conditional-on-W1" (motivic Galois would transport algebraic-cycle classes once W1 closes).
**Arbiter**: rejected. Conditional verdicts weaken the §5d story. The cell stays S with bypass→ADR-4 (cycle origin at L5/L6). If W1 closes in the future, the audit gets re-run and L3 Req 4 may upgrade.

---

## Claims that survived (no KILL)

Author's verdicts at the PAYLOAD links (L4, L5, L7, L8) largely survived. Specifically:
- L5 Req 1, 2, 4 stayed P (explicit instance holds)
- L4 Req 4 stayed Pa (FMS24 covers it)
- L4/L7/L8 O-verdicts all stayed O (walls correctly identified)
- L8 Req 2, 3 stayed Pa (classical Hodge decomposition is automatic on all smooth projective)

---

*End of kills.md. 3 WEAKENINGs + 1 UPGRADE recorded; none affects chain validity or §5d compliance.*
