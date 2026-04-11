# Point D3 — Gross-Zagier + Kolyvagin at rank 1: Verdict

**Weight:** HEAVY
**Location in preprint:** §12
**Overall rigor label:** **[THEOREM]** (Gross-Zagier, Kolyvagin) +
**[LEMMA]** (Heegner hypothesis workaround) + **VACUOUS** within
scope
**Overall verdict:** PASS with the striking observation that
rank-1 is vacuous per paper's own Remark 12.6

## Sub-question verdicts

- **(a) Gross-Zagier formula.** [THEOREM] — Gross-Zagier 1986,
  correctly stated. The formula L'(E, 1) = ĥ(P_K) · (period
  factor) is classical.

- **(b) Heegner hypothesis at conductor 32 = 2^5 in ℚ(i).**
  [LEMMA] — For y² = x³ − x, prime 2 ramifies in ℚ(i), so the
  **classical Heegner hypothesis fails** for K = ℚ(i). The paper's
  §12.2 correctly identifies this and offers two resolutions:
  (i) Yuan-Zhang-Zhang 2013 generalized Gross-Zagier (removes
      the Heegner hypothesis); OR
  (ii) Auxiliary field ℚ(√−7) where 2 splits (since −7 ≡ 1 mod 8).
  The paper **mentions both** but **does not commit to one**.
  This is sufficient for existence in the literature but not
  for a watertight proof. Internal adversarial review's Attack
  7 flags this as "WEAKENED."

- **(c) Kolyvagin bound.** [THEOREM] — For modular E with
  analytic rank exactly 1 and a non-torsion Heegner point,
  Kolyvagin 1990 gives rank ≤ 1. Combined with GZ's rank ≥ 1:
  rank = 1. Standard.

- **(d) BSD formula at rank 1.** VACUOUS per Remark 12.6 — see
  (e) below.

- **(e) Rank-1 vacuity — paper's own Remark 12.6.** **This is
  the most important finding at this point.** The paper admits:
  > "GRH for the Hecke L-function L(s, ψ) implies L(1, ψ) ≠ 0,
  > since Re(1) = 1 ≠ 1/2 places s = 1 off the critical line.
  > Since L(E, s) = L(s, χ_K) · L(s, ψ) and both factors are
  > non-vanishing at s = 1 (by GRH), we have L(E, 1) ≠ 0 for
  > every CM curve in scope. This means the analytic rank is 0
  > for all such curves, and the rank-1 case is vacuously
  > satisfied — there are no CM curves over ℚ with CM by a
  > class-number-1 imaginary quadratic field that have analytic
  > rank ≥ 1 over ℚ."
  This is a **striking self-admission**: the rank-1 case, which
  Paper 26 presents as the other half of its theorem, is
  **vacuous** within the claimed scope. The substantive content
  is entirely at rank 0 (Point D2).

- **(f) Extension to nine class-number-1 fields.** [LEMMA] — The
  argument extends uniformly; all nine fields satisfy h_K = 1
  and the bridge construction is analogous.

## Combined finding

Gross-Zagier and Kolyvagin at rank 1 are standard classical
tools, correctly cited. The Heegner-hypothesis workaround is
reasonable but under-specified (paper mentions two paths,
commits to neither).

**The most important finding:** Paper 26's Remark 12.6 admits
that, within the CM-with-h_K=1 scope, ALL curves have analytic
rank 0 (given GRH). The rank-1 case is **vacuous**. Paper 26's
rhetorical framing as "BSD at rank 0 AND rank 1" is thus
technically correct but substantively entirely rank-0.

**This is honest of the paper to state**, and it is not a
rigor error — vacuous statements are valid. But it does mean
that the "two cases" structure of Theorem 13.1 collapses to
"rank 0 only" for the claimed scope.

## Impact on the claimed result

**The rigor-level impact is light** — rank 1 is vacuous, so the
Gross-Zagier chain is a conditional that is vacuously satisfied.
The rank-0 closure (Point D2) carries the actual substantive
content.

**The rhetorical impact is significant** — readers may be misled
by the "rank 0 + rank 1" framing into thinking the paper covers
twice as much ground as it does. The paper should be more
upfront about Remark 12.6 — not hide it as a remark inside §12.4,
but state it prominently.

## Action items

1. **Commit to a specific Heegner-hypothesis resolution** for
   the test curve y² = x³ − x. Either:
   - Use ℚ(√−7) as the auxiliary field (clean, classical GZ
     applies); or
   - Cite Yuan-Zhang-Zhang 2013 for the generalized GZ with
     ramified primes.
   Pick one and commit.
2. **Move Remark 12.6 to a more prominent position** (into §1.4
   or the abstract). The rank-1 vacuity is a key structural fact
   that should not be buried.
3. **Consider restating** Theorem 13.1 as "BSD at rank 0 for CM
   curves with h_K = 1" rather than "BSD at rank 0 and 1 for ...",
   since the rank-1 part is vacuous within scope.
