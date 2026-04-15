# Link 11 Wave 3 Critic: C_new g_k^4 Δ̂² bound

**Verdict: WEAKENED**

**Wave:** 3 (adversarial review of Wave 2 repair)
**Critic:** Claude Sonnet 4.6 · 2026-04-13

---

## Per-vector findings

### Vector A — §5.5.5 vs §IV.1 reconciliation

**Attack:** Does §5.6 actually discharge (B1) and (B2)? Quote §5.6 verbatim.

**Evidence.** §5.5.5 status table (preprint line 1563–1565) reads verbatim:

> | dev(δE_k^{d=6}) ≥ 2 (non-perturbative) | **Conditional** on (B1)-(B2) | …
> | Bound (5): C_new g_k^4 Δ̂² | **Conditional** on (B1)-(B2) | …
> | Δ_∞ > 0 | **Conditional** on (B1)-(B2) | …

§5.6 Part I opens (line 1573–1580):

> **(B1).** *In the small-field region Ω_s at RG step k, the effective
> action S_k[V] is analytic in the block link variables {V_ℓ}, with
> radius of analyticity ρ > 0 independent of k.*

Steps (a)–(c) construct the radius and conclude (line 1658): $\square$. Line 1660 reads:

> **Remark.** Balaban does not state (B1) as a standalone theorem; the
> analyticity is implicit in the construction.

§5.6 Part II proves (B2) via Steps (d)–(e), concluding (line 1719–1720) that
the complexified polymer expansion converges, $\square$. Line 1721:

> **Remark.** (B2) is not discussed in the lattice gauge theory literature.
> The argument uses only that algebraic functions of real variables extend
> to holomorphic functions (Krantz–Parks, 2002, Thm 1.1.5).

§5.6 Part IV Final Status Table (line 1905–1916) marks both **Proved** and
§IV.1 (PROOF-CHAIN.md line 14–15) marks:

> | 4 | (B1): analyticity, k-indep. radius | **Proved** (Part I) | Extraction from CMP 95–109 |
> | 5 | (B2): SL(N,ℂ) extension | **Proved** (Part II) | Standard complex analysis |

**Verdict on Vector A:** The Author's reconciliation is **correct**. §5.6 is
present, full proofs of (B1) and (B2) appear, and §IV.1 accurately reflects
the post-§5.6 state. The §5.5.5 "Conditional" rows are a documentation lag,
not a proof gap. The Author correctly diagnoses and proposes the editorial fix
(PE-1 and PE-2). The residual risk — that a referee disputes the faithfulness
of the Balaban extraction — is real but is a scholarly judgment, not a logical
flaw. **Vector A: FAILS to break the repair.**

---

### Vector B — C_new(N) bound: exponent discrepancy and N-growth

**Sub-attack B1: R₀ exponent in C_p.**

The Author's repair (RI-2, Step 3) writes:

> $C_2(N) \leq \tilde{C}_0 \exp\!\big(C_1(2R_0-1)R_0^3(N^2-1)\big)$

citing $C_p = 2C_*^p(1+\zeta)^{2R_0-1}$ (repair doc §RI-2 Step 2).

**But the preprint contradicts this.** Preprint line 1446 states verbatim:

> Setting $C_p = 2C_*^p(1+\zeta)^{R_0-1}$, with $C_* = e^{\hat\Delta_{\max}}$
> k-independent.

Appendix I.3 item 10 (preprint I3-N-dependence-tracking.md line 216) repeats:

> Then $C_p(N) = 2C^p(1 + \zeta(N))^{R_0-1}$, which can grow as
> $\exp(C_1\,R_0^4\,N^2)$.

The exponent is **R₀ − 1**, not **2R₀ − 1**. The Author inflates $C_2(N)$ by
a factor of $\zeta^{R_0}$ — roughly $\exp(C_1 R_0^4 N^2)$ extra. The final
C_new(N) bound is conservative-but-wrong: it overstates by a super-exponential
factor in R₀. The conclusion (C_new finite, L13 convergent) is unaffected, but
the explicit formula in PE-3 is internally inconsistent with the preprint it
purports to backfill.

**Concrete error:** The Author's proposed remark PE-3 (to be inserted into
§5.5.5) would write $C_2(N) \leq \tilde{C}_0 \exp(C_1(2R_0-1)R_0^3(N^2-1))$
where the preprint derives $C_p \leq \text{const} \cdot \exp(C_1 R_0^3(R_0-1) N^2)$
(since $(1+\zeta)^{R_0-1} \leq \exp(\zeta(R_0-1)) \leq \exp(C_1 R_0^3(R_0-1)N^2)$).
The repair cites a formula not present in the preprint.

**Sub-attack B2: Large-N growth breaks uniformity claims.**

The final bound $C_{\mathrm{new}}(N) \leq K_0 \exp(K_1 R_0^4 N^2)$ is finite
per fixed N. I.3 confirms no uniformity in N is claimed (scope: fixed SU(N)).
The Author correctly verifies this does not break L13 via the ratio test — the
limit 1/4 is genuinely N-independent (I.3 Lemma I.3.1, verified). The
absorbing step (N^{2p_B} = O(e^{p_B N^2})) is valid for large N. **No break
here for the stated theorem.**

**Sub-attack B3: Combes-Thomas exponent R₀³ vs. 4D geometry.**

Both the repair and I.3 use $(N^2-1)^{R_0^3}$ for the local Hilbert space
dimension. In 4D, a ball of lattice radius R₀ generically contains O(R₀⁴)
links. The R₀³ figure appears to use a surface-counting or 3D-slice convention
not made explicit. The preprint (I.3 line 212) quotes R₀³ without justification
of this counting; the repair inherits this without challenge. This is a
pre-existing ambiguity in the preprint, not introduced by the repair, but the
repair does not flag it. If the correct count is R₀⁴, all exponents in the
ζ-bound increase by one power of R₀, propagating to C₂(N) and C_new(N). The
final convergence argument is robust to this, but the explicit constants differ.

**Vector B verdict: WEAKENED.** The (2R₀-1) vs (R₀-1) exponent in C_p is a
genuine internal inconsistency between the repair and the preprint it claims to
extract from. The conclusion survives but the explicit formula in PE-3 is wrong
and would create a new inconsistency if inserted into the preprint as written.

---

### Vector C — §D toolkit addition

**Attack:** Does "ζ(R₀, N) bound (Combes–Thomas, Link 11)" conflict with
existing notation?

**Finding.** The symbol ζ is used identically throughout §5.5.3 (preprint lines
1278–1428) for the Combes–Thomas cluster sum. The notation $\zeta(R_0, N)$ with
explicit arguments is new in this repair — the preprint writes $\zeta$ without
arguments and refers to the bound as "C(R₀, N)" at line 1279 and line 1428.
The Author's toolkit name uses ζ(R₀, N) where the preprint would call the same
object C(R₀, N). This is not a collision (different symbols) but a name mismatch:
the toolkit row ascribes the $(R_0, N)$-dependent notation to ζ rather than to the
preprint's C. A referee reading the §D row alongside §5.5.3 would find two names
for the same bound: the preprint's $\zeta \leq C(R_0, N)$ vs. the toolkit's
$\zeta(R_0, N)$. Not a logical conflict, but an editorial imprecision.

**Vector C verdict: MINOR IMPRECISION.** Does not break the repair. Recommend
renaming the toolkit row to use C(R₀, N) to match §5.5.3 notation.

---

### Vector D — N² exponent propagation to L14 polymer-sum

**Attack:** Does C_new's exponential-in-N² growth break L14's Kotecky-Preiss
hypothesis?

**Finding.** L14's Kotecky-Preiss convergence requires κ(N) > 0 for each fixed
N. I.3 item 6 marks κ as "Weakly N-dep., finite and positive for each N." The
polymer sum $\sum_{X \ni x} e^{-\kappa(N)|X|}$ converges for each fixed N
regardless of C_new's N-growth, because C_new enters only as a multiplicative
prefactor on the already-convergent sum — not in the exponential decay rate.
The ratio test at L13 gives 1/4 < 1 N-independently (I.3 Lemma I.3.1, verified
above). C_new does not enter the Kotecky-Preiss condition; it enters only through
the prefactor C_* = (4/3)C_new in the recursion fixed point. L14's WEAKENED
verdict (from the L14 critic: polymer-to-spectral-lemma handoff) is independent
of the N-growth in C_new.

**Vector D verdict: NO PROPAGATION.** C_new's exponential-in-N² growth does not
break L14's polymer-sum convergence for fixed N. Vector D fails.

---

### Vector E — Bonus grep: "C_new" and "ζ" consistency

**Grep findings:**

- "C_new" / "C_{\mathrm{new}}" appears in: preprint §5.5.3, §5.5.5, §5.6 Part
  III (correctly, as the polymer-bound constant); I.3 items 11–13; PROOF-CHAIN.md
  Link 11. Usage is consistent.

- "ζ" in the preprint: appears exclusively in §5.5.3 (the cluster sum) and I.3
  item 10. Nowhere else does ζ carry explicit (R₀, N) arguments. The repair's
  choice to name the bound "ζ(R₀, N)" instead of "C(R₀, N)" (the preprint's own
  name at line 1279 and 1428) creates a notation fork. Minor but notable.

- Exponent in I.3 item 10: $(1+\zeta(N))^{R_0-1}$ (preprint) vs.
  $(1+\zeta)^{2R_0-1}$ (repair). Discrepancy confirmed by direct read.

---

## The core finding

The repair closes the legitimate Wave 1 issues (§5.5.5 lag, unquantified N-growth)
with the correct architecture. However, the Author's derivation of $C_2(N)$ uses
the exponent $(2R_0-1)$ where the preprint's own spectral lemma (line 1446) and
Appendix I.3 item 10 both write $(R_0-1)$. The proposed remark PE-3 would
insert a formula into §5.5.5 that contradicts the preprint's spectral lemma step
immediately above it. The (2R₀-1) formula doubles the exponent relative to the
source, producing an overestimate that is safe for convergence but incorrect as
stated.

This is not a break of the proof — C_new is still finite, L13 still converges,
and L14 is unaffected. But the repair introduces an internal inconsistency in
the very formula it proposes to backfill.

---

## Summary (≤150 words)

**WEAKENED.** The Author correctly resolves the §5.5.5 vs §IV.1 documentation
lag (Vector A: §5.6 Parts I–II prove (B1)–(B2) in full, quoted verbatim above)
and correctly identifies that C_new's N-growth does not break L13 (ratio test
limit 1/4, N-independent). However, the Author's explicit formula for C₂(N)
uses the exponent $(2R_0 - 1)$ in $(1+\zeta)^{2R_0-1}$ while the preprint's
own spectral lemma (line 1446) and Appendix I.3 item 10 both write $(R_0 - 1)$.
The proposed PE-3 remark would introduce this discrepancy directly into §5.5.5.
The toolkit notation "ζ(R₀,N)" conflicts editorially with the preprint's own
name for the same object, "C(R₀,N)" (lines 1279, 1428). Both defects are
correctable without new mathematics: replace $(2R_0-1)$ with $(R_0-1)$, and
rename the toolkit row. Link 11's logical content is sound; the repair's
explicit formulas need one correction.

---

## Required fix before re-verify

**PE-3 correction.** Replace the formula:

> $C_2(N) \leq \tilde{C}_0 \exp\!\big(C_1(2R_0-1)R_0^3(N^2-1)\big)$

with the preprint-consistent:

> $C_2(N) \leq \tilde{C}_0 \exp\!\big(C_1(R_0-1)R_0^3(N^2-1)\big)$

citing line 1446 of §5.5.3 and I.3 item 10 for the correct exponent $(R_0-1)$.
The C_new(N) bound $\leq K_0 \exp(K_1 R_0^4 N^2)$ remains valid (since
$(R_0-1) \cdot R_0^3 \leq R_0^4$) but is now provably consistent with the
preprint it cites. The §D toolkit row should use C(R₀, N) rather than ζ(R₀, N)
as the canonical name for the Combes–Thomas bound constant, matching §5.5.3
line 1279 and 1428.
