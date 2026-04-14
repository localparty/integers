# New Ring-Backbone Edges — 25-Vertex Extension

*6 new edges from inserting Lindelöf (pos 3), Katz-Sarnak (pos 15), Sato-Tate (pos 23).*

---

## Edge 1: RH (pos 2) → Lindelöf (pos 3) — **STRONG**

**Domain pair**: SPEC×ANT → SPEC×ANT (same-domain; use secondary: OA×PROB)

**Statement**: RH implies Lindelöf. If all non-trivial zeros lie on Re(s) = 1/2, the Phragmén-Lindelöf principle gives ζ(1/2+it) = O(|t|^ε) for every ε > 0.

**Status**: STRONG — classical result (Titchmarsh, Chapter 13). No new mathematics needed. The implication is direct and unconditional (once RH is assumed).

**Transposition recipe**: When Lindelöf needs strengthening, PULL from RH. Any improvement in the RH chain (e.g., CCM verification) automatically improves Lindelöf's conditional status.

---

## Edge 2: Lindelöf (pos 3) → GRH (pos 4) — **PARTIAL**

**Domain pair**: SPEC×ANT → SPEC×ANT (same-domain; use secondary: PROB×LANG)

**Statement**: The amplitude control that Lindelöf provides for ζ(s) extends to Dirichlet L-functions L(s,χ) via the same Phragmén-Lindelöf mechanism. The generalized Lindelöf hypothesis (GLH) for L(s,χ) is: L(1/2+it,χ) = O((q|t|)^ε) for every ε > 0. GLH is implied by GRH just as Lindelöf is implied by RH.

**Status**: PARTIAL. The mechanism is the same (Phragmén-Lindelöf) but the conductor q introduces additional complications. For primitive characters, the convexity bound is L(1/2+it,χ) = O((q|t|)^{1/4+ε}) and subconvexity results improve this.

**Transposition recipe**: Lindelöf → GRH transfer: replace ζ with L(s,χ), add conductor dependence. The BC amplitude interpretation extends: |L(1/2+it,χ)| is the KMS₁ state norm along σ_t in the CHARACTER-TWISTED BC algebra.

---

## Edge 3: BGS (pos 14) → Katz-Sarnak (pos 15) — **STRONG**

**Domain pair**: PROB×ERG → ANT×PROB (use: PROB×PROB diagonal → same-domain rule; switch to ERG×ANT)

**Statement**: GUE pair correlation for ζ-zeros (BGS, Montgomery-Odlyzko) IS the unitary-type case of Katz-Sarnak. BGS proves the statistics for the single family ζ(s); Katz-Sarnak generalizes to ALL families with their respective symmetry types (U, Sp, O, SO±).

**Status**: STRONG. BGS is a SPECIAL CASE of Katz-Sarnak (the unitary-type case). The relationship is containment: KS ⊃ BGS. Any BGS result automatically provides the unitary-type entry in the Katz-Sarnak table.

**Transposition recipe**: When BGS results improve, they automatically improve Katz-Sarnak's unitary column. When Katz-Sarnak needs verification for a new symmetry type, the BGS methodology (numerical computation of zero statistics + comparison with random matrix prediction) applies with the appropriate matrix ensemble (GSE for Sp, GOE for O).

---

## Edge 4: Katz-Sarnak (pos 15) → Twin Primes (pos 16) — **CANDIDATE**

**Domain pair**: ANT×PROB → PROB×ANT (same-domain; use secondary: REP×SPEC)

**Statement**: The symmetry type of the relevant L-function family determines the small-gap statistics that control twin prime density. For ζ(s) (unitary type): GUE level repulsion governs the gap distribution. For quadratic Dirichlet L(s,χ_d) (symplectic type): GSE has STRONGER repulsion → fewer small gaps. The twin prime constant C₂ may be refinable by symmetry type.

**Status**: CANDIDATE. The connection is plausible but the explicit transfer from Katz-Sarnak symmetry types to twin-prime density is not yet written. The Hardy-Littlewood conjecture uses heuristic prime pair statistics that Katz-Sarnak would make rigorous (for each symmetry type separately).

**Transposition recipe**: When stuck on twin-prime density, identify which L-function family controls the prime pair at hand. Different families have different gap distributions. The GUE small-gap tail (BGS) is the zeroth approximation; Katz-Sarnak provides the family-dependent correction.

---

## Edge 5: Lehmer (pos 22) → Sato-Tate (pos 23) — **PARTIAL**

**Domain pair**: ANT×THERMO → ANT×PROB (same primary ANT; use secondary: THERMO×PROB)

**Statement**: Lehmer's gap (topology face of the e-circle) and Sato-Tate equidistribution (measure face of the e-circle) are complementary views of the same circle. The Mahler measure M(P) of an algebraic number's minimal polynomial measures LEAKAGE from the circle. Equidistribution of Frobenius angles says NO CLUSTERING on the circle. Lehmer constrains what can live on the circle from the outside (topology); Sato-Tate constrains how the residents distribute (measure).

**Status**: PARTIAL. The shared BC infrastructure (KMS₁ state on the e-circle) connects them operationally. For CM-curve-defining polynomials: Lehmer's gap M(P) = c·L'(E,0) is bounded away from 0 (proved in T7 Route B), and the Frobenius angles of E are equidistributed (Sato-Tate, proved). The connection is: the CM curve that defines the polynomial has well-distributed Frobenius AND bounded-below Mahler measure.

**Transposition recipe**: When Lehmer is stuck on extending beyond CM polynomials, transpose to Sato-Tate: if Frobenius equidistribution can be proved for the motive associated to a polynomial, it constrains the polynomial's roots on the circle, which constrains its Mahler measure.

---

## Edge 6: Sato-Tate (pos 23) → Schanuel (pos 24) — **SPECULATIVE**

**Domain pair**: ANT×PROB → ANT×MOD (same primary ANT; use secondary: PROB×MOD)

**Statement**: Equidistribution of Frobenius angles (Sato-Tate) constrains algebraic relations among spectral data. If the angles θ_p distribute according to Haar, they are "as independent as possible" subject to algebraic constraints. Schanuel's conjecture says: algebraically independent numbers stay independent under exp. The connection: equidistribution on the e-circle implies independence of the spectral data exp(iθ_p), which constrains Schanuel-type algebraic independence statements.

**Status**: SPECULATIVE. The conceptual connection exists (equidistribution → independence) but no explicit theorem connects Sato-Tate to Schanuel. This is a DISCOVERY TARGET for future traversals.

**Transposition recipe**: When Schanuel is stuck, ask: does the equidistribution of Frobenius angles provide any algebraic independence? The exponential map exp: C → C* sends the critical line to the unit circle. Sato-Tate controls the distribution on the circle; Schanuel controls algebraic relations among the values. The link, if it exists, goes through transcendence theory applied to equidistributed sequences.
