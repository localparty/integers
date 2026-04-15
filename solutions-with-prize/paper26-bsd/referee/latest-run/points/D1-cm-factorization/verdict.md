# Point D1 — CM L-function factorization: Verdict

**Weight:** MEDIUM
**Location in preprint:** §10
**Overall rigor label:** **[THEOREM]** on Deuring; **[LEMMA]** on
Grössencharacter identification; **[KEY LEMMA — OPEN]** on "bridge
reaches L(s, ψ)"
**Overall verdict:** PARTIAL — factorization is standard, but the
bridge-reaching-ψ claim is in Point A3

## Sub-question verdicts

- **(a) Deuring 1953.** [THEOREM] — Deuring's CM factorization is
  classical and correctly cited. For E/ℚ with CM by K,
  L(E, s) = L(s, ψ) · L(s, ψ̄) where ψ is the Grössencharacter.
  Modern reference: Silverman *Advanced Topics* Ch. II.

- **(b) Grössencharacter identification.** [LEMMA] — For the test
  curve E : y² = x³ − x with CM by ℚ(i), the Grössencharacter ψ
  is uniquely determined by the action of Hecke operators on torsion
  points. The paper's §10.2 writes:
  > L(E, s) = L(s, χ_{−4}) · L(s, ψ)
  where χ_{−4} is the Kronecker character (a DIRICHLET character
  of conductor 4, living on ℤ, not a Hecke character of K).
  **Sloppy notation:** the correct Deuring factorization is
  L(E, s) = L(s, ψ) · L(s, ψ̄), not L(s, χ_K) · L(s, ψ). The
  paper's expression identifies one factor with L(s, χ_{−4}),
  which is correct only if ψ or ψ̄ equals the base change of
  χ_{−4} to K — this relationship holds in some cases but is
  not proved in the paper. Internal adversarial review's Attack
  2 flags this as "sloppy but not fatally wrong."

- **(c) Zeros of L(E, s).** [KEY LEMMA — OPEN] — Zeros of L(E, s)
  are the union of zeros of L(s, ψ) and L(s, ψ̄). GRH for L(E, s)
  requires GRH for BOTH Hecke L-functions. The paper argues this
  via the twist (§3.6.1 + §9.2 Step C). Concern inherited from
  Point A3: does the bridge actually reach Hecke character
  L-functions?

- **(d) Modularity of CM curves.** [THEOREM] — CM curves over ℚ
  are modular via Hecke theta series. Classical, predating Wiles.

## Combined finding

The CM factorization itself is standard (Deuring 1953). The
identification of the Grössencharacter for a specific test curve
is standard but the paper's §10.2 notation is sloppy, writing
the factorization in terms of χ_{−4} rather than the standard
(ψ, ψ̄) form.

The critical question — does the bridge reach L(s, ψ)? — is
inherited from Point A3 (MY3). Deuring's factorization itself
doesn't create new concerns; it just locates the problem at the
Hecke-L-function twist step.

## Impact on the claimed result

**Low at this level**, moderate inherited from Point A3. The
factorization is the vehicle that transmits GRH-for-Hecke-L to
GRH-for-L(E,s). If A3 is closed, D1 closes. If A3 is not closed,
D1 inherits the open concern.

## Action items

1. **Tighten §10.2 notation** to use the standard Deuring
   factorization L(E, s) = L(s, ψ) · L(s, ψ̄) rather than
   L(s, χ_K) · L(s, ψ). State clearly how χ_{−4} relates to ψ
   (if at all) for the specific test curves.
2. See Point A3 for the twist concern.
