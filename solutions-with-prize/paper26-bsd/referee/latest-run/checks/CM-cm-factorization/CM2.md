# Check CM2: Grössencharacter ψ identified for test curves

**Group:** CM
**Source:** Paper 26 §10.2, §14.1
**Pass criterion:** ψ uniquely determined and correctly written.

**Verdict:** PARTIAL (sloppy notation)
**Rigor label:** [LEMMA]

**Justification:** The paper writes L(E, s) = L(s, χ_K) · L(s, ψ)
in §10.2, which is a non-standard factorization. The standard
Deuring factorization is L(E, s) = L(s, ψ) · L(s, ψ̄). The
paper's version identifies one factor with the Dirichlet
character L-function L(s, χ_{−4}), which is only meaningful if
the Grössencharacter ψ or ψ̄ happens to equal the base change of
χ_{−4}. This holds in some cases but is not proved in the paper.

Internal adversarial review's Attack 2 flags this as "sloppy but
not fatally wrong" (WEAKENED). The core chain uses GRH for all
Hecke L-functions of K (Step C), which covers both L(s, ψ) and
L(s, ψ̄) regardless of how they relate to χ_K.

**Fix:** Use the standard Deuring form throughout, with explicit
Grössencharacter identification for each test curve.

**Cross-references:**
- Per-Point: D1
- Internal adversarial: Attack 2
