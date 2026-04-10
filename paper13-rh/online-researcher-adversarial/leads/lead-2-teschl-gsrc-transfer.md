# Lead 2: Teschl gsrc 2026 transfer theorem applied to CCM(N) → CCM(∞)

## Direction (written by Strategist, Cycle 1)
Status: OPEN
Pattern: Pattern 6 (projection — H_N is a projection of H_{N+1} so limits commute with spectral data) + Pattern 5 (compactness → discreteness)
Feasibility: 7/10
Rationale: Teschl-Wang-Xie-Zhou, "On Generalized Strong and Norm Resolvent Convergence" (arXiv:2601.10476, Jan 2026), gives a streamlined framework for gsrc/gnrc of self-adjoint operators on DIFFERENT Hilbert spaces with identification maps. This is exactly the tool needed to transfer CCM's finite-N spectral data into a limiting operator, and to transport our ITPFI product-state convergence into the CCM operator-norm side. Strategy/11 proposed to hand-roll Kato + spectral mapping; Teschl 2026 replaces that with an off-the-shelf theorem that additionally packages essential spectrum and spectral projection convergence.
Toolkit connection: R265 (ITPFI of ω₁ = ⊗_p ω₁^p, proved three ways) is the state-level convergence that must be transported to operator level. Strategy/11 §3 step 4 is the module this lead replaces. Cross-links: R28 (archimedean O(1/λ) estimate) bounds the archimedean identification map error.
Investigate:
1. What exactly are Teschl's gsrc hypotheses (2026 version)? Enumerate them as a checklist: identification maps J_N: H_∞ → H_N, conditions on J_N, resolvent-compatibility, etc.
2. For CCM(N) → CCM(∞): what are the natural H_N, H_∞, and J_N? The L²([λ⁻¹,λ]) spaces may be FIXED while N varies (if λ is fixed), in which case the identification is the identity and Teschl simplifies to classical gsrc. Alternatively, if λ_N → ∞, the spaces genuinely vary. Which is the right regime?
3. Check each hypothesis explicitly against the CCM family: does D(λ,N) have uniformly bounded resolvent norms? Does the resolvent difference go to zero strongly? Is essential spectrum absent (so spec = discrete, Teschl's strongest conclusions apply)?
4. If one hypothesis fails, is there a WEAKER Teschl-type result (ascent/descent, or the non-selfadjoint Boegli / 2511.20971 version) that still delivers the limit spectrum?
5. Can the ITPFI product-state ω₁^{≤P_N} = ⊗_{p ≤ P_N} ω₁^p be converted into an identification map via the GNS construction, so that Teschl's J_N becomes an explicit formula rather than an abstract existence?
Would close if: all Teschl hypotheses are verified for the CCM family, the limit D_∞ exists self-adjoint with essential spectrum empty, and the limit spectrum is the limit of the CCM spectra (which, if lead 1 closes, is critical-line at each finite stage).
Would kill if: either (a) Teschl's hypotheses fundamentally FAIL (e.g. loss of resolvent compactness in the limit because CCM's perturbation accumulates too fast), OR (b) the limit has non-empty essential spectrum that absorbs the desired discrete spectrum.
Source: arXiv:2601.10476 (downloaded: sources/teschl-gsrc-norm-resolvent-2026.pdf). Backup paper: arXiv:2511.20971 (ascent-descent SRC stability, non-selfadjoint insurance).
Premise check: The relevant invariant under N-perturbation is the location of the discrete spectrum. gsrc is non-vacuous for discrete spectrum transfer precisely when the essential spectrum stays bounded away from the discrete spectrum of interest — that is the "gap condition." The executor must verify THIS gap is positive uniformly in N, otherwise the transfer is vacuous (lim σ_disc(D_N) could be empty or absorbed into σ_ess). Kill #8 (type III₁ uniqueness ≠ compactness) is the cognate warning here: an abstract uniqueness does not automatically give resolvent compactness. We need explicit compactness in the ID space L²([λ⁻¹,λ]), not an abstract algebraic statement.

---

## Research (appended by Executor, Cycle 1)
[placeholder — executor fills in]

---

## Adversarial (appended by Adversary, Cycle 1)
[placeholder — adversary fills in]
