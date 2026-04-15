# RH Compliance Audit — Critic Attacks (run-02)

*For each author verdict, the critic proposes an alternative OR confirms. Only dissents are itemized; remaining 87 cells are CONFIRM (critic agrees with author).*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Critic pass discipline

For each cell, the critic asks:
- Is the verdict too strong? (downgrade proposal)
- Is the verdict too weak? (upgrade / strengthen proposal)
- Is the citation precise to §-level? (if not: STRENGTHEN-CITE)
- Does the verdict miss a named wall (if SILENT, should it be O instead)?
- Is the action (for SILENT) routed to the correct programme addressing?

11 dissents raised. The remaining 87 cells pass CONFIRM.

---

## §1 Dissents (11)

### D1. L1 Req 3 — author **Pa** → critic **S**

**Critic**: L1 CCM construction doesn't explicitly invoke the functional equation at statement level. FE underlies ξ(s) symmetry but L1's own content is operator-theoretic (E_N^+ Hilbert space, D_N self-adjoint). The Pa verdict overstates — L1 uses ξ-structure but doesn't assert / prove anything about analytic continuation. Downgrade to S, BYPASS→ADR-3 (classical at B_bare §5 programme entry).

**Alternative**: S with bypass→ADR-3.

### D2. L1 Req 4 — author **P** → critic **Pa**

**Critic**: L1 constructs D_N on E_N^+, which is the even-function subspace where ξ lives. The exclusion of trivial zeros at −2, −4, … happens because the even-function restriction + Γ(s/2)-pole cancellation in ξ automatically excludes trivial ζ-zeros. BUT this is structural-by-construction; L1 doesn't give a standalone theorem stating "trivial zeros excluded". Author's P is the locus-where-it-happens claim; Pa is more faithful to what L1 explicitly proves. Downgrade to Pa — the explicit triv/non-triv theorem is at L6.

**Alternative**: Pa (not P).

### D3. L2 Req 3 — author **Pa** → critic **S**

**Critic**: Analogous to D1. L2's ITPFI + KMS_1 + Weil form convergence uses analytic continuation of local ζ-factors AND the functional equation, but the FE is an ambient prerequisite, not a L2-layer content. Downgrade to S, BYPASS→ADR-3.

**Alternative**: S with bypass→ADR-3.

### D4. L3a Req 3 — author **Pa** → critic **S**

**Critic**: Γ-factor enters archimedean tail estimate as a fact-about-ξ, not a FE-in-L3a assertion. The tail is about decay rates of eigenfunctions, not a statement about analytic continuation. Downgrade to S, BYPASS→ADR-3.

**Alternative**: S with bypass→ADR-3.

### D5. L3b Req 5 — author **Pa** → critic **S**

**Critic**: Eigenvector approximation rate O(log λ / λ) is a chain-internal quality metric; its "consistency with Odlyzko precision" is marketing prose, not a theorem-level claim. Downgrade to S (the numerical check is at L6 output, not L3b quality bound).

**Alternative**: S with bypass→ADR-5 (L6 output consistency).

### D6. L3d Req 5 — author **Pa** → critic **P**

**Critic**: ρ ≥ 4.27 is a specific quantitative pin uniform in N with caveat-resolved status. This is more than "consistency" — it's a concrete quantitative prediction that anchors the numerical-consistency axis at the chain level. Upgrade to P.

**Alternative**: P (not Pa).

### D7. L4c Req 1 — author **Pa** → critic **S**

**Critic**: L4c spectral exactness is about spec(D_∞) = lim spec(D_N). It does not itself conclude RH — that's at L6. Pa verdict ("feeds directly into L6 RH QED") overstates: "feeds into" is not "partially addresses". Downgrade to S, BYPASS→ADR-1 (L6).

**Alternative**: S with bypass→ADR-1.

### D8. L5 Req 7 — author **Pa** → critic **S**

**Critic**: L5 Hurwitz convergence is about ξ̂_N → Ξ uniformly on compacts. The Weil-explicit-formula structure is carried by Ξ but not re-stated at L5. The author's "indirect carrying" reasoning is too weak for a Pa verdict. Downgrade to S, BYPASS→ADR-7 (L2).

**Alternative**: S with bypass→ADR-7.

### D9. L5 Req 3 — author **P** → critic **Pa** (WEAKEN)

**Critic**: L5 Hurwitz uses the FE implicitly (Ξ(t) is the FE-symmetric form), but "uses" ≠ "proves" the FE. The FE is classical input at the programme entry, not re-proved at L5. Downgrade to Pa. L5 IS the layer where FE is used most visibly, but the verdict should reflect "uses", not "proves".

**Alternative**: Pa (not P).

### D10. L5 Req 5 — author **Pa** → critic **Pa** (CONFIRM but strengthen citation)

**Critic**: Confirm Pa. Strengthen citation to explicitly list Odlyzko T < 2 × 10²⁰ data tables + van de Lune–te Riele–Winter first-1.5 × 10⁹ results as the comparison target. Author's citation is too general.

**Alternative**: Pa with STRENGTHEN-CITE (p13§L5 + Odlyzko 1987/2001 + vdL-tR-W 1986).

### D11. S1 Req 5 — author **Pa** → critic **Pa** (CONFIRM but strengthen citation)

**Critic**: Confirm Pa. Strengthen citation: AE simplicity cert N ≤ 20 is in paper13-rh; Slepian limit N > 20 extension. Odlyzko observation that all computed ζ-zeros are simple is the numerical fact being matched. Add Odlyzko simple-zeros observation citation.

**Alternative**: Pa with STRENGTHEN-CITE.

---

## §2 STRENGTHEN-only dissents (confirm verdict, sharpen citation) — 0 additional beyond D10/D11

All other cells either have adequate citation or are SILENT with routine BYPASS action.

---

## §3 Critic summary

- **11 dissents raised**
- **4 downgrades S← Pa** (D1, D3, D4, D5, D7, D8 — wait, 6 downgrades: D1, D3, D4, D5, D7, D8)
- Let me recount: D1 (L1 Req 3: Pa→S), D3 (L2 Req 3: Pa→S), D4 (L3a Req 3: Pa→S), D5 (L3b Req 5: Pa→S), D7 (L4c Req 1: Pa→S), D8 (L5 Req 7: Pa→S) = **6 Pa→S downgrades**
- **1 downgrade Pa← P** (D9: L5 Req 3)
- **1 downgrade Pa← P** (D2: L1 Req 4)
- **1 upgrade P← Pa** (D6: L3d Req 5)
- **2 CONFIRM-with-STRENGTHEN-CITE** (D10, D11)

Total: 6 + 1 + 1 + 1 + 2 = **11 dissents**. ✓

## §4 Critic §5d meta-check

Even if ALL 6 Pa→S downgrades are accepted by arbiter, post-critic Core 1-5 coverage remains:
- Req 1: was 4 non-SILENT; minus L4c → 3 non-SILENT (L1 O, L5 Pa, L6 O). PASS.
- Req 2: was 1 non-SILENT (L6 Pa). PASS.
- Req 3: was 5 non-SILENT (L1, L2, L3a, L5, L6); minus L1, L2, L3a → 2 non-SILENT (L5 Pa, L6 Pa). Still ≥ 1. PASS.
- Req 4: was 4 non-SILENT; minus nothing (D2 just downgrades P→Pa within non-SILENT) → still 4 non-SILENT. PASS.
- Req 5: was 5 non-SILENT (L3b, L3d, L5, S1, L6); minus L3b → 4 non-SILENT. PASS. AND L3d upgrades Pa→P via D6.
- Req 7: was 3 non-SILENT (L2, L5, L6); minus L5 → 2 non-SILENT (L2 P, L6 Pa). PASS.

Post-critic §5d compliance: **preserved on all Core requirements 1–5 and Optional 7**. Req 6 remains SILENT-as-column (acceptable for optional).

---

*End of critic-attacks.md. Proceeding to arbiter-decisions.md.*
