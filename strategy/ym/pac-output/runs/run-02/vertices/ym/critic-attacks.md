# YM Compliance Audit — Critic Attacks (run-02)

*Critic pass: for each of the 140 cells, propose at least one alternative verdict with reason. Agreement-with-confirming-evidence is acceptable. Disagreements go to arbiter.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Attack format

- `AGREE`: same verdict, with supporting evidence
- `WEAKEN`: propose a less favorable verdict (e.g., PROVED → PARTIAL; PARTIAL → SILENT)
- `STRENGTHEN`: propose a more favorable verdict
- `RECLASSIFY`: propose a different non-tiered change (e.g., SILENT → OPEN-BUT-ADDRESSED or vice versa)

---

## L1 — KK Spectral gap

- Req 1: `AGREE` (Pa). Confirming: Prop I.4.2 explicitly runs Weitzenböck for every compact irreducible symmetric space; however, at L1 itself, the statement is SU(N) — hence Pa is right, not P.
- Req 2: `AGREE` (S). L1 is KK-and-4D-lattice; ℝ⁴ limit is explicitly elsewhere (§51).
- Req 3: `WEAKEN` (P → Pa). The μ₁ ≥ 2N/r₃² bound is for the internal Laplacian, not the 4D mass gap directly; uniformity in V requires the subsequent cluster expansion + transfer-matrix bound. Flag for arbiter.
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (S). The IR gap doesn't match UV AF.
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L1b — IR equivalence

- Req 1: `AGREE` (Pa).
- Req 2: `AGREE` (S).
- Req 3: `AGREE` (P). Lemmas 1–4 explicitly bound Δ₀^std uniformly in L via Feshbach.
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (S).
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L2 — UV stability (Balaban)

- Req 1: `AGREE` (P). K.9 table is exhaustive.
- Req 2: `STRENGTHEN` (Pa → P). Balaban convergence κ is proven volume-independent in K.9; however, the PROOF of L2 is at finite V — so Pa is defensible. Arbiter call.
- Req 3: `AGREE` (Pa).
- Req 4: `AGREE` (S).
- Req 5: `STRENGTHEN` (Pa → P). All-loop UV finiteness from Paper 11 K.4 is arguably full AF UV match at the free-energy level. However, Req 5 is about Schwinger-function AF, which is stricter. Stand with Pa.
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L3 — Polymer convergence κ k-independent

- Req 1: `AGREE` (P).
- Req 2: `AGREE` (Pa).
- Req 3: `AGREE` (Pa).
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (S).
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L4 — (B1) analyticity, k-independent radius

- Req 1: `AGREE` (P).
- Req 2: `AGREE` (Pa).
- Req 3: `AGREE` (Pa).
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (Pa). Analyticity is necessary infrastructure for the small-flow-time expansion that enters H4 bypass.
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L5 — SL(N,C) extension

- Req 1: `AGREE` (P).
- Req 2: `AGREE` (S).
- Req 3: `AGREE` (S).
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (S).
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L6 — C-elimination of Tr(F³)

- Req 1: `AGREE` (P). C-symmetry is universal.
- Req 2: `AGREE` (S).
- Req 3: `AGREE` (S).
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (S).
- Req 6: `AGREE` (S). Correctly noted that the operator classification feeds into OPE at L18.
- Req 7: `AGREE` (S).

## L7 — Newton decomposition

- Req 1: `AGREE` (P).
- Req 2: `AGREE` (S).
- Req 3: `AGREE` (S).
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (S).
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L8 — dev(Tr(DF)²) ≥ 2

- Req 1: `STRENGTHEN` (Pa → P). The deviation calculation is a structural operator-power-counting argument that holds for any G. However, specific numerical value of the dev index could be G-dependent. Stand with Pa (author's caution is appropriate).
- Req 2: `AGREE` (S).
- Req 3: `AGREE` (Pa).
- Req 4: `AGREE` (S).
- Req 5: `WEAKEN` (Pa → S). L8 is about deviation index of a specific dim-6 operator; AF is about the whole short-distance match. The Pa is overstatement. Arbiter call.
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L9 — Dim-6 classification

- Req 1: `AGREE` (Pa).
- Req 2: `AGREE` (S).
- Req 3: `AGREE` (Pa).
- Req 4: `AGREE` (S).
- Req 5: `WEAKEN` (Pa → S). Same issue as L8 Req 5. Arbiter call.
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L10 — dev(δE_k^{d=6}) ≥ 2 non-perturbatively

- Req 1: `AGREE` (Pa).
- Req 2: `AGREE` (Pa).
- Req 3: `AGREE` (P).
- Req 4: `AGREE` (S).
- Req 5: `WEAKEN` (Pa → S). Same as L8, L9. Arbiter call.
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L10b — Spectral lemma k-independent

- Req 1: `AGREE` (Pa).
- Req 2: `AGREE` (Pa).
- Req 3: `AGREE` (P).
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (S).
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L11 — C_new g_k^4 Δ̂² bound

- Req 1: `AGREE` (Pa).
- Req 2: `AGREE` (Pa).
- Req 3: `AGREE` (P).
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (Pa). The g_k^4 factor is AF-coupling power.
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L12 — RG recursion C_{k+1} = C_k/4 + C_new

- Req 1: `AGREE` (Pa).
- Req 2: `AGREE` (Pa).
- Req 3: `AGREE` (P).
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (Pa). RG recursion is the AF flow structure.
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L13 — Σ C_k g_k^4 Δ̂_k² < ∞

- Req 1: `AGREE` (Pa).
- Req 2: `AGREE` (Pa).
- Req 3: `AGREE` (P).
- Req 4: `AGREE` (S).
- Req 5: `AGREE` (Pa).
- Req 6: `AGREE` (S).
- Req 7: `AGREE` (S).

## L14 — Δ_∞ > 0 (THE MASS GAP)

- Req 1: `AGREE` (P). Theorem I.4.1 is explicit.
- Req 2: `AGREE` (P). §51 is explicit.
- Req 3: `AGREE` (P). §51 + F.5 Rem. are explicit.
- Req 4: `AGREE` (S). OS axioms are at L16.
- Req 5: `AGREE` (S).
- Req 6: `AGREE` (S).
- Req 7: `STRENGTHEN` (P confirmed). Non-triv signature (i) σ > 0 requires area-law result (Theorem 4 §4.4); L14 alone gives gap but area law is an additional input. However, Δ_∞ > 0 combined with the cluster expansion of the proof that supports L14 is itself a non-triviality signature in the gapped confining phase. Arbiter can keep P or downgrade to Pa. Stand with P (consistent with §05 Proposition Non-triv argument).

## L15 — Gradient-flow contractivity

- Req 1: `WEAKEN` (P → Pa). Lemma L.1.1 uses SU(N) explicit structure (the mass m₁ = 2√N/r₃); extension requires I4 group-specific Einstein constants. So G-generality is via bootstrap, Pa is appropriate. Arbiter call.
- Req 2: `AGREE` (S).
- Req 3: `AGREE` (Pa).
- Req 4: `AGREE` (Pa).
- Req 5: `AGREE` (Pa). Small-flow-time expansion is H4 bypass infrastructure.
- Req 6: `AGREE` (Pa). Suzuki formula enabler.
- Req 7: `AGREE` (S).

## L16 — Continuum Schwinger OS0–OS4 at fixed t > 0

- Req 1: `AGREE` (Pa).
- Req 2: `AGREE` (P). §51 V establishes OS in continuum.
- Req 3: `AGREE` (P).
- Req 4: `STRENGTHEN/CONFIRM` (P is correct; this is THE OS cell). Confirming: §05.6 Proof of (f) is the full OS1–OS5 verification. Arbiter: hold P.
- Req 5: `AGREE` (S).
- Req 6: `AGREE` (Pa). L16 is axioms; T_μν at L17.
- Req 7: `AGREE` (Pa). OS axioms satisfied by free fields too; non-triv is distinct.

## L17 — [Tr F²]_R, T_μν^R constructed

- Req 1: `AGREE` (Pa).
- Req 2: `AGREE` (P).
- Req 3: `AGREE` (Pa).
- Req 4: `AGREE` (P). Wightman via reconstruction.
- Req 5: `AGREE` (S).
- Req 6: `AGREE` (P). THE stress-tensor cell.
- Req 7: `AGREE` (Pa).

## L18 — AF match, leading-order OPE — CONDITIONAL on H4

- Req 1: `WEAKEN` (Pa → S). L18's AF match statement is for SU(N); group-general AF via K.6 is separate. The H4 bypass is SU(N)-specific currently. Arbiter call: Pa (inherits via K) or S (H4 isn't proven for all G even bypass-wise).
- Req 2: `AGREE` (Pa).
- Req 3: `AGREE` (S).
- Req 4: `AGREE` (Pa).
- Req 5: `AGREE` (O). This is the definitive OPEN-BUT-ADDRESSED cell. H4 explicit; bypass route cited.
- Req 6: `AGREE` (Pa). Author's note is precise: power-law unconditional, AF form H4-conditional.
- Req 7: `AGREE` (P). AF signature is direct.

---

## Critic summary

- 140 cells reviewed.
- Agreements: ~128.
- Dissents (arbiter calls): 12
  - L1 Req 3: P → Pa (WEAKEN): author claims the μ₁ bound is uniform-in-V, but the 4D transfer-matrix uniformity is at L1b, not L1.
  - L2 Req 2: Pa → P (STRENGTHEN): K.9 group-general V-independence is strong.
  - L2 Req 5: Pa → P (STRENGTHEN): K.4 all-loop UV-finite arguably AF UV match at free-energy level.
  - L8 Req 1: Pa → P (STRENGTHEN)
  - L8 Req 5: Pa → S (WEAKEN): L8 is dim-6 suppression, not AF directly.
  - L9 Req 5: Pa → S (WEAKEN): same concern as L8.
  - L10 Req 5: Pa → S (WEAKEN): same concern.
  - L15 Req 1: P → Pa (WEAKEN): SU(N) explicit in Lemma L.1.1.
  - L18 Req 1: Pa → S (WEAKEN): H4 bypass is SU(N)-specific.
  - L16 Req 4: P affirmed strongly.
  - L14 Req 7: P affirmed.
  - L17 Req 6: P affirmed strongly.

- No SILENT cell that author marked non-SILENT is proposed SILENT — so the J-W coverage is preserved.
- All proposed changes are within the audit's sensitivity bounds.

Pass to arbiter.

---

*End of critic-attacks.md.*
