# BSD Compliance Audit — Kills (run-02)

*Claims WEAKENED or CLARIFIED by this compliance audit, including the two BROKEN items from Paper 26 adversarial run-01 that are carried over into the B_bare framing and the citation-tightenings for the 5 WEAKENED items from that run.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Scope

Paper 26 adversarial run-01 (2026-04-09, 15 attacks: 8 SURVIVED / 5 WEAKENED / 2 BROKEN) identified presentation-level fixes that the compliance audit now propagates into the compliance map verdicts and flags for the B_bare synthesis (next run). This file records each.

This `kills.md` is for compliance-audit-originated WEAKENINGs and carry-overs; it does NOT invalidate the BSD chain. The chain's 11/11 link-closure holds.

---

## Kill 1 — "Unconditional" framing forbidden at L11 (carry-over of BROKEN 1)

- **Prior language** (initial preprint draft + author draft verdict at L11): "BSD Theorem 13.1 is proved **unconditionally** for CM h_K=1 rank {0,1}."
- **Adversarial run-01 finding** (Attack 1 — Circularity / conditionality): The chain inherits CBB axioms from Paper 13 RH infrastructure and Paper 23. It is conditional on CBB, same status as the Paper 13 RH chain. "Unconditional" is an overclaim. BROKEN.
- **Audit propagation**: Arbiter Decision 8 forces L11 verdicts Req 1, 2, 4 P to carry the rider "(conditional on CBB p23)". All L7, L9, L10 P / Pa verdicts inherit the same rider (except LITERATURE-class L cells which are unconditional because modularity / Kolyvagin / Deuring are themselves unconditional).
- **Effect**: compliance-map verdicts correctly labelled. No chain invalidation.
- **B_bare implication**: §2 and §15 of B_bare (per brief DELTA 5) must use "conditional on the CBB axioms inherited from paper13-rh, which carry the same status as in Paper 13." Never "unconditional."

## Kill 2 — Curve 32.a3 c_2 = 4 (not 1) — carry-over of BROKEN 2 — RESOLVED

- **Prior datum** (earlier preprint draft numerics table): Tamagawa c_2 = 1 for curve 32.a3 (E: y² = x³ − x).
- **Adversarial run-01 finding** (Attack 14 — Sha formula verification at specific curve): LMFDB lists 32.a3 with c_2 = 4, not 1. The BSD formula check as written reduces by a wrong factor of 4. BROKEN.
- **Resolution status** (verified 2026-04-14 at `solutions-with-prize/paper26-bsd/nodes/K-bsd-theorem.md`): node K numerical-verification table now reads "Tamagawa c_2 | 4 (LMFDB 32.a3; corrected from earlier draft)". The formula check ⟨RHS = 1·Ω·1·4 / 16 = Ω/4 = L(E,1)⟩ is verified exactly (both sides ≈ 0.65551438).
- **Audit status**: RESOLVED at the node level. The compliance-map L11 Req 4 cell verdict P rests on the corrected numerics.
- **B_bare implication**: §18 Numbers Table (per brief DELTA 5) MUST use c_2 = 4 for 32.a3. Any future run that regenerates numerics tables must pull LMFDB-verified data.

## Kill 3 — L10 Req 7 verdict misplaced O → Pa (new in this audit)

- **Prior suggestion** (first author draft): L10 (Gross-Zagier rank 1) was labelled **O** for Req 7 on the reasoning that rank is part of the Wiles "any rank r ≥ 0" requirement.
- **Audit finding**: L10 PROVES rank 1 via GZ + Kolyvagin (LITERATURE). The scope-wall W_rank (for r ≥ 2) belongs at L11 where the scope-disclosure lives. Placing O at L10 misattributes the wall to a proof layer.
- **Arbiter Decision 7**: L10 Req 7 WEAKENED from author's O to **Pa** (rank 1 in scope; r ≥ 2 is W_rank at L11).
- **Effect**: cell verdict corrected. Does not affect coverage — W_rank is still disclosed at L11. Does not affect chain validity.

## Kill 4 — L1 and L2 Req 6 S → Pa (scope fingerprint, new in this audit)

- **Prior suggestion**: L1 and L2 are about construction of the BC algebra over K and the bridge family over K respectively; not directly about elliptic-curve breadth. First author draft: S for Req 6.
- **Audit finding**: The h_K = 1 restriction (L1) and the explicit 355-triple enumeration over K (L2) are SCOPE-RESTRICTION FINGERPRINTS visible at each layer. Pa, not S (per YM pilot discipline on scope visibility).
- **Arbiter Decisions 1, 2**: Pa confirmed. Not a weakening but a strengthening-of-coverage correction.
- **Effect**: Req 6 column gains 2 non-SILENT cells (L1, L2 upgraded S→Pa).
- **Chain validity**: unaffected (cells now more accurately coded).

## Kill 5 — L7 Req 2 Pa → P (direct discharge, new in this audit)

- **Prior suggestion**: L7 GRH is a zero-localisation claim; full c ≠ 0 discharge was reserved for L11. First author: Pa.
- **Audit finding**: GRH ⇒ s = 1 not on Re(s) = 1/2 ⇒ L(E, 1) ≠ 0 ⇒ c ≠ 0 in analytic-rank-0 case. This is DIRECT discharge at L7, not merely an ingredient feeding L11. P-class at layer of origin, per YM pilot discipline (L14 Req 7 signature P-class).
- **Arbiter Decision 3**: Pa → P (conditional on CBB).
- **Effect**: Req 2 column now has 2 P cells (L7, L11).

## Kill 6 — L8 Req 3 Pa → L and L9 Req 5 Pa → L (LITERATURE promotion)

- **Prior suggestion**: Author rated both cells Pa (partial contribution).
- **Audit finding**: BCDT 2001 (modularity — giving L-continuation for every E/Q) and Kolyvagin 1990 (rank-0 Sha finite) are PUBLISHED, PEER-REVIEWED, WIDELY-CITED literature theorems that fully discharge the requirement at the layer where they are invoked. LITERATURE-class L is the correct verdict, not Pa.
- **Arbiter Decisions 5, 6**: Pa → L.
- **Effect**: compliance-map more accurately reflects discharge strength. Req 3 column: 2 L cells. Req 5 column: 1 L cell.

---

## Carry-overs from Paper 26 adversarial run-01 WEAKENED items (citation tightenings, not kills per se)

The 5 WEAKENED items (not BROKEN) carry over as citation-tightening instructions for B_bare synthesis (next run), not as verdict changes in this audit's compliance map. Enumerated here for audit completeness:

### WEAKENED 1 — CM factorisation notation (Attack 2)

- **Tightening**: Cite Deuring 1953 explicitly at L8 Req 3 cell; format: "L(E, s) = L(s, ψ) · L(s, ψ̄) for CM E/K (Deuring 1953; paper26 Step 8; Silverman Advanced Topics, Ch. II, Theorem II.10.5)."
- **Applied**: in audit-draft L8 and in the compliance-map L8 Req 3 cell's L-class citation.

### WEAKENED 2 — Ha-Paugam construction precision (Attack 3)

- **Tightening**: Cite Ha-Paugam 2005 at L1; format: "A_{BC, K} = C*(K^{ab}) ⋊ I_K with unique KMS_1 state for h_K = 1 imaginary quadratic (Ha-Paugam 2005 §3 Theorem 3.1; paper26 Step 1 / Node A)."
- **Applied**: in audit-draft L1.

### WEAKENED 3 — Meyer-over-K precision (Attack 4)

- **Tightening**: Cite Connes-Marcolli extension at L5 twist argument; format: "|Δc^ψ(δ)| < 2/(N-1) for all Hecke characters ψ (paper26 Step 5c; Connes-Marcolli 2008 for GL₂-twist framework)."
- **Applied**: in audit-draft L5 Req 2.

### WEAKENED 4 — Heegner hypothesis for Gross-Zagier (Attack 7)

- **Tightening**: Cite Yuan-Zhang-Zhang (YZZ) for Heegner hypothesis generalisation at L10; format: "Gross-Zagier 1986; Yuan-Zhang-Zhang for Heegner-hypothesis-relaxing generalisation to higher-genus Shimura curves." Per W_hK bypass route.
- **Applied**: in audit-draft L10 Req 4, Req 6; compliance-map L10 cells.

### WEAKENED 5 — Twist argument for L(s, ψ) (Attack 11)

- **Tightening**: Cite Connes-Marcolli twist framework at L7 (for GL(2) extension path); format: "Connes-Marcolli GL₂ system (Connes-Marcolli 2008) extends BC machinery from Hecke-character-twisted GL(1) to GL(2), enabling W_nonCM bypass." Per W_nonCM bypass route.
- **Applied**: in §3.2 W_nonCM disclosure.

### WEAKENED 6 — Rank-1 leading-coefficient formula (Attack 13)

- **Tightening**: Cite Rubin 1991 for explicit rank-1 leading coefficient at L9/L10/L11; format: "c* at rank 1 = 2 · Ω · R · ∏ c_p · |Sha| / |tors|² explicit via height pairing (Rubin 1991 Lemma 4.6; Gross-Zagier 1986)."
- **Applied**: in audit-draft L9 Req 4, L10 Req 4.

---

## No other kills

All other cells are consistent between Paper 26 adversarial run-01, the PROOF-CHAIN, and this compliance audit. The chain's 11/11 link structure holds intact.

## Confidence impact

- Chain confidence (paper26-bsd PROOF-CHAIN.md): 9/10 unchanged.
- CBB-conditionality rider: applied; matches Paper 13 RH.
- §5d compliance: PASS (every Wiles requirement column has ≥ 1 non-SILENT cell).
- Four named walls (W_rank, W_nonCM, W_hK, W_Sha): confirmed and disclosed with DELTA-10 fields.

---

## Pin #6 J_CKM side-note (not a kill; recorded for completeness)

PROOF-CHAIN §"Known gap": L4 (Step 4 dark-state impossibility) is a cocycle-shift Hasse-Brauer-Noether inequality, NOT a J_CKM vertex evaluation. The (k, N) = (4, 41) bridge-family row at L2 is a ℚ(i) Brauer invariant — a terminology coincidence with the CKM k = 4 vertex, not a hidden identity. Pin #6's structural anchor for J_CKM × 10⁵ = log(γ_1) · ζ(3) is `integers/paper12-cbb-system/research/102` via the Mellin bridge, not paper26 Step 4.

This note is OUT OF SCOPE for the 7-requirement compliance audit (it's a cross-programme pin audit, not a Wiles requirement). Recorded for commit-memo completeness; no chain-link status change.

---

*End of kills.md.*
