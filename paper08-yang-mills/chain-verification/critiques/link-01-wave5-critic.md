# Link 1 Wave 5 Adversarial Critic

**Target:** KK spectral gap Δ₀^KK > 0 (Thm 4) — Wave 4 Author patch (Route B)
**Wave:** 5 (independent verification — different instance from Wave 2/4 Authors)
**Verdict:** **SURVIVED**
**Confidence:** 9/10

---

## Bootstrap sources

- `nodes/L1-patch.md` — Wave 4 Route B patch
- `critiques/link-01-wave3-critic.md` — Wave 3 findings (four attack vectors)
- `preprint/sections/04-lattice-proof-part1.md` — live preprint text (Theorem 4 at lines 749–783; Theorem 1 at lines 182–255)
- `preprint/sections/A-laplacian-spectrum.md` — Appendix A full text

**Note on preprint state.** The live preprint (04-lattice-proof-part1.md) still carries the
Wave 2 text: Theorem 4 statement at line 751 reads `r_3/a < \sqrt{3/(4N)}` and the proof
sentence at line 783 repeats it. Remark 3 is not yet present in the file, and Remark 2 has
not been updated. The Wave 4 L1-patch.md proposes three edits (Edit 1, Edit 2 Parts A and B,
Edit 3). All checks below evaluate the proposed edits as stated in the patch.

---

## C1 — Route B removes the falsified β_max claim

**Finding: PASSES.**

Wave 3 demonstrated that at the boundary r₃/a = √(3/(4N)), β_max < 0 for all N ≥ 2
(N=2: β_max ≈ −1.58; N=3: β_max ≈ −1.83). The falsification was decisive.

Route B replaces the Theorem 4 statement (Edit 2, Part B) as follows:

**FROM:** "with r₃/a < √(3/(4N))"
**TO:** "under the assumption r₃/a ≪ 1 (i.e. a ≫ r₃, which holds throughout the
physical regime a ≥ 10⁻²⁰ m ≫ r₃ ∼ 10⁻³¹ m)"

The β_max assertion in the new statement reads:

> "where β_max ∼ m₁a/6 ∼ 10¹⁴ in the physical regime; the condition r₃/a ≪ 1 ensures β_max > 0"

This is correct. Under r₃/a ≪ 1, m₁a = 2√N · a/r₃ ≫ 1, so m₁a/6 ≫ ln(c_d K C₀^{1/6})
for any fixed finite logarithmic factor. The equivalence m₁a ≫ 1 ↔ r₃/a ≪ 1 relies on
m₁ = 2√N/r₃ (Ikeda–Taniguchi exact value for CP^{N-1}); the patch correctly flags in
Self-suspicion §3 that the conservative form would use the Weitzenböck lower bound
m₁ ≥ √(2N)/r₃, giving m₁a ≥ √(2N) · a/r₃ ≫ 1. This is a residual precision issue
but does not affect the verdict: both the exact value and the Weitzenböck lower bound
tend to +∞ as r₃/a → 0, so β_max > 0 is secured under either form.

The falsified O(1) threshold is no longer asserted. The β_max > 0 claim is now contingent
only on r₃/a ≪ 1, which is verified by eleven orders of magnitude in the physical regime.

**C1 verdict: the falsified β_max claim is removed. Route B is valid.**

---

## C2 — Appendix A cross-reference N-generalized

**Finding: PASSES.**

Wave 3 (Attack Vector A, residual issue) identified that Remark 2's phrase "the (p,q) = (0,0)
mode of Appendix A" is CP²-specific: Appendix A is explicitly titled "The Laplacian Spectrum
on CP²" and uses SU(3) Dynkin labels (p,q) throughout (verified in A-laplacian-spectrum.md,
lines 1–30). For N ≠ 3 the (p,q) notation is undefined.

Edit 1 (L1-patch.md, §"Revised preprint edits") replaces the Remark 2 leading sentence with:

> "The constant zero mode of the scalar Laplacian on CP^{N-1} is present as a classical
> modulus of the Fubini–Study family but is not quantized in this construction."

The (p,q) notation is retained only as an explicit parenthetical for N=3, marked
"CP²-specific; for general N it is simply the constant function." Independent verification
against A-laplacian-spectrum.md confirms:

- Row (0,0) of the A.2 table labels the zero eigenvalue as "Trivial (vacuum)" — the
  constant eigenfunction (line 37).
- The Remark on N-dependence (lines 16–23) correctly states that the general-N first
  non-trivial eigenvalue is 4N/r₃² (Ikeda–Taniguchi), and the (p,q) labels are SU(3)-specific.

The proposed Edit 1 language ("constant zero mode of the scalar Laplacian on CP^{N-1}") is
correct for all N ≥ 2 and matches the terminology used in Appendix A's own N-remark.

**C2 verdict: Appendix A cross-reference is correctly N-generalized. PASSES.**

---

## C3 — C₀(N) Remark 3 marked "worst-case"

**Finding: PASSES.**

Wave 3 (Attack Vector B, §B3) found that the Wave 2 Edit 2 formula for C₀(N) set
γ = c′_N (an O(1) spectral gap eigenvalue), effectively dropping the (a/r₃)^{−2(N−1)²}
suppression present in the full mode sum where γ = c′_N · a/r₃. This gave the worst-case
bound without labelling it as such, and then used this worst-case C₀ alongside the small
m₁a/6 ∼ 0.77 — two incompatible choices.

Edit 2, Part A (L1-patch.md) replaces the Remark 3 header and content as follows:

> **Remark 3 (Explicit worst-case bound for C₀(N)).**
> ...This formula is the worst-case bound, achieved as a/r₃ → 1⁺; at larger a/r₃ the actual
> value of C(N) carries an additional (a/r₃)^{−2(N−1)²} suppression factor from the
> mode-sum integral (see Step 4).

The "worst-case" designation is now explicit. The Change note removes the erroneous claim
"which exceeds ln(c_d K C₀^{1/6}) for all N ≥ 2 at the stated physical regime r₃/a ≪ 1"
from the β_max assertion and removes the erroneous numerical check at the threshold boundary.
The self-suspicion §2 (L1-patch.md) correctly notes a residual risk: a reader may ask why a
worst-case formula at a/r₃ → 1 is given when the theorem assumes a/r₃ ≫ 1. The answer is
that C₀ is defined as a supremum over the allowed range (preprint lines 564–566), so the
worst-case formula is the definition — it bounds C₀ for all a/r₃ ≥ 1. This logic is sound.
A clarifying sentence in a future author pass would help but is not required for verdict.

**C3 verdict: Remark 3 is marked "worst-case" as Wave 3 required. PASSES.**

---

## C4 — Downstream lemma dependency on the dropped threshold

**Finding: NO BROKEN DEPENDENCY.**

The check requires determining whether any downstream link among L1b, L3, L4, L10, L10b,
L14 assumes r₃/a < √(3/(4N)) explicitly.

**Structural finding.** Wave 3 (Attack Vector D) and the chain-state file
(`chain/chain-state.md`, line 116) both confirm: C₀ enters the KP criterion only through
β_max in Link 1. The bond-activity bound (Link 1) is the unique injection point of C₀ and
the convergence threshold into the proof chain.

**L1b, L3, L10, L10b** (no node files exist in `nodes/`): These links have critic files
(`link-01b-critic.md`, `link-03-critic.md`, `link-10-critic.md`, `link-10b-critic.md`)
but no patch or repair nodes, indicating they passed in Wave 1 and were not revisited.
Independent grep of all chain-verification files (excluding L1 files) finds zero occurrences
of `r_3/a.*sqrt`, `sqrt.*3.*4N`, or `3/(4N)` outside the L1 documents and chain-state
summary. No downstream link references the threshold.

**L4 (nodes/L4-repair.md, nodes/L4-patch.md):** L4 concerns the Kotecký–Preiss convergence
parameter κ' and the small-field condition. The repair checks κ' = κ − 2log(1+ζ) > log 8
and ζ → 0 under asymptotic freedom. No reference to r₃/a < √(3/(4N)) in either file.
L4 depends on κ (a Balaban RG constant, O(1) in physical units) and ζ (the polymer
activity), not on the KK sector threshold.

**L14 (nodes/L14-repair.md, nodes/L14-patch.md):** L14 concerns the Cluster-Balaban
Handoff and the C₀^{cl} constant from §5.4.6 polymer bounds. The `link-14-wave3-critic.md`
and repair files confirm C₀^{cl} is a distinct cluster-expansion constant (line 128 of
L14-repair.md explicitly notes this), not the KK bond-activity C₀ from Theorem 2. No
reference to r₃/a < √(3/(4N)) appears in any L14 file.

**Mechanism summary.** The threshold r₃/a < √(3/(4N)) appeared only in the statement and
proof of Theorem 4 (lines 751, 783 of the live preprint). Its downstream consequence was
only β_max > 0, which is consumed at the KP-criterion step (Link 1). All downstream links
take as input the fact that β_max > 0 (i.e., that there exists a valid coupling range), not
the specific numerical value of the threshold. Replacing the threshold with r₃/a ≪ 1
changes the domain statement of the theorem but leaves the logical input to every downstream
step unchanged: β_max > 0 remains asserted (now correctly) under the new hypothesis.

**C4 verdict: no downstream lemma carries a broken dependency on the dropped threshold. PASSES.**

---

## Residual items (non-blocking)

**Seiler proposition number (HONEST-STALL, unchanged).** The mathematical argument for
the adjoint-extension (Ad(U) isometry → transfer-matrix equivalence) is sound per Wave 3's
independent verification. The proposition number within Seiler 1982 LNP 159 remains
unverified. Deferred to bibliography pass per Wave 4. Not a logical hole.

**Weitzenböck vs. Ikeda–Taniguchi in the proof sentence (Self-suspicion §3).** The
updated proof sentence uses m₁ = 2√N/r₃ (exact eigenvalue). A conservative form would
use m₁ ≥ √(2N)/r₃ (Weitzenböck lower bound). Both give m₁a ≫ 1 under r₃/a ≪ 1; the
distinction is numerically immaterial in the physical regime but should be harmonized
in a future author pass for formal precision.

**"r₃/a ≪ 1" quantitative boundary (Self-suspicion §1).** Route B replaces a wrong
O(1) bound with an asymptotic hypothesis. A sharp explicit lower bound on a/r₃ in terms
of c_d, K, and C₀(N) remains Route A's province and is deferred. For the purpose of this
proof (which targets r₃/a ∼ 10⁻¹⁵), the asymptotic hypothesis is adequate. A referee
pressing for an explicit numerical lower bound is a reasonable concern but does not
constitute a broken link.

---

## Summary (≤150 words)

All four checks pass. C1: Route B correctly removes the falsified β_max > 0 claim at the
O(1) threshold and replaces it with the honest hypothesis r₃/a ≪ 1; under this hypothesis
β_max > 0 is secured for all finite c_d, K, C₀(N). C2: Edit 1 replaces the CP²-specific
(p,q) = (0,0) cross-reference with "constant zero mode of the scalar Laplacian on
CP^{N-1}", valid for all N ≥ 2. C3: Remark 3 now carries the "worst-case (a/r₃ → 1)"
label Wave 3 required and removes the erroneous threshold numerical check. C4: No
downstream link (L1b, L3, L4, L10, L10b, L14) assumes r₃/a < √(3/(4N)) explicitly;
the threshold was consumed only at the KP step internal to Link 1. Three minor residual
items (Seiler citation, Weitzenböck/exact-eigenvalue harmonization, quantitative ≪ 1
bound) are non-blocking. Link 1: **SURVIVED**.

---

*Wave 5 complete. Verdict: SURVIVED (Route B accepted; WEAKENED → REPAIRED). Three
non-blocking residuals flagged for bibliography and future author passes.*
