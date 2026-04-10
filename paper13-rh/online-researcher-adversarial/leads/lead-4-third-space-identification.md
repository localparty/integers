# Lead 4: The "third space" — explicit Mellin identification H₁ ∩ (scaling sector) ↪ L²([λ⁻¹,λ])

## Direction (written by Strategist, Cycle 1)
Status: OPEN
Pattern: Pattern 1 (geometric reinterpretation — the BC scaling representation IS CCM's L²([λ⁻¹,λ]) representation, in different coordinates) + Pattern 6 (projection)
Feasibility: 6/10
Rationale: Strategy/10 §6 angle E asked for a THIRD Hilbert space H_new with (a) Euler-product factorization so ITPFI applies and (b) spectrum containing {γ_n}. CCM's L²([λ⁻¹,λ]) is one candidate. The ω₁ GNS space H₁ is another (but has the wrong spectrum {log n}). This lead asks the STRUCTURAL question: is there a canonical Mellin / scaling-representation identification that embeds a PROPER SUBSECTOR of H₁ into CCM's L²([λ⁻¹,λ]) in a way that preserves the Euler-product factorization? If yes, we have a direct transport of ITPFI into CCM — lead 3's bound becomes a corollary, and the wall in strategy/10 is physically dissolved rather than just bypassed.
Toolkit connection: CCM 2024 prolate wave paper (arXiv:2310.18423) defines the Sonin space, which is the Mellin image of functions vanishing on [−1,1] — essentially the target of the transport. The BC scaling operator D_BC in the scaling representation is −i·x·∂_x in Mellin coordinates, and acts on L²((0,∞), dx/x) which restricts to L²([λ⁻¹,λ], dx/x). R265 (ITPFI) gives the factorization on the source side.
Investigate:
1. Write down the scaling-representation action of A_BC on L²((0,∞), dx/x) explicitly. What is the Borchers decomposition here, and does it still factor over primes?
2. Identify the Mellin transform map L²([λ⁻¹,λ]) → Mellin side, and check whether CCM's D(λ,N) on L²([λ⁻¹,λ]) is the Mellin image of a truncated product operator ⊗_{p≤P_N} D^p on the BC scaling sector.
3. If yes, the transport isometry is explicit and the p-local factorization of ω₁ = ⊗_p ω₁^p transports to a p-local factorization of CCM's operator. State the resulting theorem.
4. Check the Sonin-space condition: CCM 2024 uses the Sonin space (Mellin image of functions vanishing on [−1,1]) as the ambient space for the prolate operator. Is the scaling-rep Hilbert space of A_BC the Sonin space in disguise, or a parent of it?
5. If NO canonical identification exists, document WHY. Specifically: which structural obstruction (non-faithfulness of the scaling rep, non-isomorphism of the Mellin transforms, etc.) blocks it, and whether that obstruction is a technical artifact or a deep obstruction analogous to the H₁-vs-H_R wall.
Would close if: an explicit isometry (Sector of BC scaling rep) → L²([λ⁻¹,λ]) that intertwines BC Euler factorization with CCM's prime-by-prime rank-one build-up. Such a map would be a MAJOR structural result independently of RH.
Would kill if: the BC scaling rep has the WRONG measure (e.g. Haar dx/x vs Lebesgue dx) in a way that Mellin transform cannot reconcile, OR the Borchers decomposition becomes trivial under Mellin and no prime factorization survives.
Source: CCM prolate wave 2024 (sources/ccm-prolate-wave-2024.pdf), CCM zeta spectral triples 2025 (sources/ccm-zeta-spectral-triples-2025.pdf), research/265 (ITPFI), paper12 §anchor-document (BC scaling rep).
Premise check: The identification is non-vacuous IFF the scaling-rep Hilbert space carries a genuine prime factorization that maps ISOMORPHICALLY to CCM's rank-one structure (as opposed to just "both are Hilbert spaces"). The invariant that shifts under variation of primes is the DIMENSION of the range of the truncated rank-N perturbation — a discrete, computable quantity. The executor must verify this dimension matches on both sides (BC truncation and CCM truncation) and doesn't just "agree at the level of cardinalities." Kill #13 (ITPFI gives spec(H_mod) = {log n}) is the warning: one cannot naively import ITPFI into a new representation without checking what OPERATOR it now controls. Here the operator is D_BC in the scaling rep, NOT the modular Hamiltonian — that's the reason this doesn't collapse back onto the 18-kill wall.

---

## Research (appended by Executor, Cycle 1)
[placeholder — executor fills in]

---

## Adversarial (appended by Adversary, Cycle 1)
[placeholder — adversary fills in]
