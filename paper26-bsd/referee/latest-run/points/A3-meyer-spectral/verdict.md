# Point A3 — Meyer spectral inclusion over Q(i): Verdict

**Weight:** HEAVY
**Location in preprint:** §3.6, §3.6.1, §9.2 Step C
**Overall rigor label:** **[KEY LEMMA — OPEN]** (two sub-items)
**Overall verdict:** CLOSABLE GAP — substantial work required

## Sub-question verdicts

- **(a) Meyer's precise statement.** [THEOREM] (as background)
  — Meyer 1997/2005 proves the distributional spectral inclusion
  for the Bost-Connes operator over Q. Standard and correctly
  cited.

- **(b) Extension to ζ_K.** **[KEY LEMMA — OPEN]** — Paper 26
  Proposition 3.6 asserts the extension "by the same argument
  with Λ replaced by Λ_K." The proof is a sketch, not a proof.
  The essential step is re-verifying Meyer's distributional-
  support construction for the Dedekind zeta explicit formula.
  This is plausible (the structure is identical) but the paper
  does not do the work. No references to Connes-Consani-Marcolli
  extensions to number fields are cited.

- **(c) Extension to L(s, ψ) via twist.** **[KEY LEMMA — OPEN]**
  — Proposition 3.6.1 asserts a "twisted spectral realization"
  following Connes-Marcolli 2008 §4.3. Two issues:
  (i) CM 2008 §4.3 constructs the twist over **Q**, not over K;
      the extension to K is not carried out.
  (ii) The paper's argument that "the cocycle shift is
       insensitive to the twist because |ψ(𝔭)| = 1" is a
       first-order statement. At higher order, the character
       phase contributes, and the paper does not verify that
       the integrality argument survives at the exact level.

- **(d) Distributional vs genuine eigenvalues.** **[KEY LEMMA — OPEN]**
  — Meyer gives distributional eigenstates, not point spectrum.
  The distributional-to-genuine upgrade is the classical wall
  of the Bost-Connes approach to GRH. Paper 26 asserts the
  upgrade via Nelson but does not prove that the distributional
  eigenstates lie in the point spectrum of the self-adjoint
  closure. This is the same concern that motivated Paper 13 v2
  to pivot to CCM+ITPFI+Bögli+Hurwitz.

- **(e) Scope of the spectral inclusion.** Tied to (b), (c), (d);
  same concerns.

## Combined finding

**This is one of the three most critical issues in the audit.**
Paper 26 claims that the Bost-Connes spectral method over Q(i)
captures the zeros of Hecke L-functions L(s, ψ) as **genuine
eigenvalues** of a self-adjoint operator. The claim is
**structurally plausible** but **not proved** in the preprint.

The necessary work:
1. Write out Meyer's proof for ζ_K carefully.
2. Construct the twisted BC operator T_{BC,K}^ψ over K
   explicitly, following Connes-Marcolli §4.3.
3. Prove the twisted distributional spectral inclusion.
4. Prove the distributional → genuine point spectrum upgrade
   (this is the classical wall).

None of these is carried out in Paper 26. All are asserted by
analogy.

## Impact on the claimed result

**Critical.** Without this upgrade, the bridge cannot reach
L(s, ψ), and the entire chain from the Bost-Connes spectral
method to GRH for CM L-functions collapses. The downstream
Kolyvagin + Gross-Zagier applications would then have no GRH
input.

**Alternative architecture:** Paper 13 v2 abandoned the Meyer-
Nelson route in favor of CCM + ITPFI + Bögli + Hurwitz. Paper 26
does NOT use this alternative. If the Meyer-Nelson route cannot
be rigorously extended to K, Paper 26 would need to either:
(a) do the distributional-to-genuine upgrade rigorously, or
(b) adopt the CCM architecture and extend CCM to number fields
    (which does not yet exist in the literature).

## Action items

1. Write out a rigorous extension of Meyer 1997 to ζ_K — either
   inline in the paper or as a separate companion paper.
2. Construct the twisted T_{BC,K}^ψ operator explicitly.
3. Address the distributional-to-genuine upgrade explicitly, either
   by:
   - Proving a trace-formula argument for K, or
   - Citing Connes-Consani work on number field spectral realization
     (if such work exists), or
   - Adopting the CCM architecture.

**Estimated effort:** Multiple months of focused work by an expert
in non-commutative geometry and analytic number theory.
