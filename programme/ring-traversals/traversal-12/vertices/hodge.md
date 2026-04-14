# T12 Vertex 10: Hodge — L4 Full-Closure Assessment

*Type C | Confidence: 3/10 (full), 5/10 (CM abelian varieties) | Date: 2026-04-14*

## L4 current state (from PROOF-CHAIN.md line 16)

**Status:** `PARTIAL (LITERATURE-with-scope for abelian-variety-powers slice; OPEN for general BC-motivated class)`. arXiv:2510.21562 (2024) proves Grothendieck standard conjecture D (hom = num) for powers of abelian varieties over algebraically closed fields in pure Chow motives. T5 briefly upgraded to CONDITIONAL-STRONG; T6 VERIFY correctly reverted to PARTIAL.

## What arXiv:2510.21562 adds to L4

Direct content: D closed for the class `{A^n : A abelian variety, n ≥ 1}`. Via the BSD-CM bridge (Paper 26), CM elliptic curves E land as 1-dim abelian varieties, so h¹(E)^{⊗n} and more generally the CM-abelian powers orbit inherit D. This strictly covers the BSD-CM intersection slice, which is the most programme-relevant piece of L4.

## Can L4 be upgraded PARTIAL → ESTABLISHED?

**No — scope-gap is real.** L4 as written targets the **BC-motivated** class (the image of the CCM endomotive functor under Links 1-3). arXiv:2510.21562 targets the **abelian-variety-powers** class. These classes intersect on CM-type objects but are not identified: the endomotive functor factors through the motivic Galois category, and no literature theorem shows its image lands in abelian variety powers. To upgrade, one would need either:

  (a) a proof that every BC-motivated variety is a motive of an abelian variety power (essentially: the BC algebra's motivic Galois group is a subgroup of ∏ MT(A_i) for some abelian A_i — plausible but unproved), or
  (b) a restatement of L4 that restricts to the abelian-variety-powers slice from the outset (trivially ESTABLISHED, but weakens the chain target).

**Verdict:** L4 stays `PARTIAL`. Recommended refinement: split L4 into **L4a (abelian-variety-powers slice, ESTABLISHED via arXiv:2510.21562)** and **L4b (BC-motivated extension, OPEN pending Link 3 plus image characterisation)**. This is bookkeeping precision, not a closure.

## Remaining wall for general Hodge

Four real walls remain, in increasing order of depth:

1. **L3 (Hodge filtration compatibility).** G_mot action on H*_dR must preserve F^p for BC-motivated X. Deep conjecture in motivic cohomology; no partial closure. **Gates Route I entirely.**
2. **L4b (standard conjecture D beyond abelian-variety-powers).** Open for general BC-motivated class. Gated on L3 anyway.
3. **L6/L7 (Langlands bridge + Route composition).** Gaitsgory-Raskin 2024 supplies the categorical equivalence; extracting Hodge-class algebraicity from Aut(Bun_G) ~ QCoh(LocSys_G^L) is the unresolved geometric-to-categorical dictionary.
4. **L8 (motivic functoriality to all smooth projective).** Every smooth projective X must admit a motivic correspondence to a BC-motivated variety preserving (p,p)-classes. **As hard as the Hodge conjecture itself** (the chain attack plan §8 flags this).

## Move

Vertex Hodge L4: `PARTIAL` **unchanged**. Record L4a/L4b split as bookkeeping refinement in PROOF-CHAIN (optional for T12; functional status is identical). No confidence change: still 3/10 (full), 5/10 (CM abelian vars). Momentum stays on GRH and PvNP for T12; Hodge awaits a Link 3 breakthrough before any real closure motion.
