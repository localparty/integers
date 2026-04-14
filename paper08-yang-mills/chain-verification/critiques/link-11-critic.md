# Link 11 Critic Verdict: C_new g_k^4 Δ̂² bound

**Verdict: WEAKENED — conditional flag confirmed; one latent gap on C_new N-uniformity**

## Attack-by-attack summary

**AV1 — g_k^4 in the non-perturbative regime.** The g_k^4 factor enters
in two places: (a) from the Balaban operator-norm bound ||E_k|| ≤ C g_k^4
(CMP 109 inductive hypothesis, cited as "Literature"); (b) from the
non-perturbative suppression e^{−c/g_k^2} ≤ g_k^4 on the asymptotically
free trajectory. Both are valid only in the small-field region Ω_s and
for k ≥ k_0 where g_k^4 ≤ 1/(4C_B). Steps k < k_0 are handled by a
bounded-constant remark (§5.5.3 Step 3, Section 5.7 Remark 1). The
quartic form is not a purely perturbative artefact; it is the Balaban
inductive bound. Attack fails.

**AV2 — Lattice Δ̂ vs. continuum Δ_∞.** The text is explicit (line 16
of §5.5.1): Δ̂_k = a_k Δ_phys = a* Δ_phys · 2^{−k} is the dimensionless
lattice gap, and Δ̂_{k+1}² = Δ̂_k²/4. The bound is stated in lattice
variables throughout. The connection to the continuum gap Δ_∞ is made in
Section 5.7 (RG recursion and limit). No conflation between lattice and
continuum gaps occurs in the statement of Link 11. Attack fails.

**AV3 — k-independence of C_new.** The paper assembles C_new = C_2 · C
where C_2 is the spectral-lemma constant C_p at p = 2, and C is the
Balaban operator-norm prefactor. §5.5.3 Step 3 proves C_p = 2C_*^p
(1+ζ)^{2R_0−1} with C_* = e^{Δ̂_max} and ζ ≤ C(R_0,N) both k-independent;
this is Link 10b. The Balaban constant C is also k-independent by the
inductive structure (L=2, d=4, SU(N), m_W fixed). C_new is therefore
k-independent — BUT the formula C_p = C_p(p, R_0, N) depends on N. The
paper acknowledges N-dependence (line 1199) but never states C_new is
uniform in N. For a fixed SU(N) proof (N=2 or N=3) this is irrelevant;
for a claim uniform in N it would need statement. This is a minor gap
but not a gap for the stated theorem. Attack partially lands as a
precision defect, not a logical error.

**AV4 — Tightness and impact on RG recursion (Link 12).** The bound
C_new g_k^4 Δ̂² feeds into the RG recursion C_{k+1} = C_k/4 + C_new
(Link 12, §5.4). The factor of 1/4 comes from Δ̂_{k+1}² = Δ̂_k²/4.
The recursion has a fixed point C* = (4/3)C_new and the telescoping
sum converges (Link 13). Whether the bound is tight or has slack does
not affect the summability argument, only the numerical value of C*.
The RG recursion does not require tightness. Attack fails.

**AV5 — Uniformity in N.** C_p depends on N (explicitly stated at line
1199); C_new = C_2 · C therefore inherits N-dependence. The theorem
(Theorem 8) is stated for fixed SU(N), so this is fine for the stated
result. However, the N-dependence of C_new through ζ ≤ C(R_0, N) is
not quantified. If C(R_0, N) grows with N, C_new could diverge in the
large-N limit, invalidating any large-N extrapolation. The paper does
not claim N-uniformity, so this is not a gap in the stated theorem —
but it is unaddressed. Attack fails for the stated theorem; flag stands.

## Core finding: conditional status not resolved

The status table at §5.5.5 explicitly marks Bound (5): C_new g_k^4 Δ̂²
as **Conditional** on (B1)–(B2) (line 1564). The proof chain table at
§IV.1 (line 1918) marks Link 11 as **Proved**, citing "Spectral lemma +
Steps 10, 10b." This is an internal inconsistency: §5.5.5 says
Conditional, §IV.1 says Proved. The resolution is that §5.6 claims to
prove (B1)–(B2), so after §5.6 the conditionality is discharged. But
(B1) is described as extracted from Balaban CMP 95–109 via a "remark"
(line 1660: "Balaban does not state (B1) as a standalone theorem"),
and (B2) is noted as "not discussed in the lattice gauge theory
literature" (line 1721). These are author-constructed claims, not
direct citations of proved theorems.

**The conditional flag is real.** Link 11 is proved given (B1)–(B2),
but (B1)–(B2) are themselves non-standard claims reconstructed from
Balaban's series. The verdict must reflect this.

## Conclusion

AV1, AV2, AV4 fail cleanly. AV3 reveals a precision gap (C_new
N-dependence unquantified) that does not break the stated theorem but
should be flagged. AV5 fails for fixed N. The dominant weakness is
inherited from Links 10/10b: the bound is **conditionally proved**,
contingent on (B1)–(B2) which are author-reconstructed rather than
directly cited theorems.

**WEAKENED** — bound is conditional on (B1)–(B2); internal
inconsistency between §5.5.5 (Conditional) and §IV.1 (Proved) should
be resolved by explicitly marking Link 11 as Proved-given-(B1)-(B2).
C_new N-dependence should be quantified if large-N applications are
intended.
