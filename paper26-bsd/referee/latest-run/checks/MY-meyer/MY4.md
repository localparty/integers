# Check MY4: Distributional → genuine spectrum upgrade

> **☑ CLOSED 2026-04-10 (same day) via Route 3 — G's KMS projector
> bypass.**
>
> MY4 is the classical Meyer–Nelson wall. It was bypassed by the
> observation that the bridge argument of Paper 26 §§6–8 never
> actually needed the distributional → genuine upgrade. The
> dependency was rhetorical (§6's eigenstate framing), not
> logical. G's projector `P_k^𝔭 := I − s_𝔭^k (s_𝔭^k)^* ∈ A_{BC,K}`
> has algebraic KMS_1 expectation `ω_1^K(P_k^𝔭) = 1 − N(𝔭)^{−k}`,
> which is exactly the dark-state bound of §6 DS1 expressed at the
> C*-algebra level with no reference to eigenstates. Combined with
> Paper 26 Remark 7.2 ("the derivation is pure algebra on the
> local Euler factor") and Hasse–Brauer–Noether local–global
> reciprocity, the entire §9.2 Step B argument is eigenstate-free.
>
> **Final rigor label: [LEMMA] unconditional.** The distributional
> → genuine upgrade is not needed for Paper 26's proof chain.
>
> See `strategy/05-route3-kms-projector-bypass.md` and
> `research/route3-kms-projector-bypass.md` for the full argument.
> Numerical sanity check: `referee/code/test_projector_P.py`.
>
> *The r01 verdict below is preserved as the initial audit state.*

---

**Group:** MY
**Source:** Paper 26 §3.6 + §3.7 combined
**Pass criterion:** Meyer distributional eigenstates become genuine
point-spectrum eigenvalues of T̄_{BC,K}.

**Verdict (r01):** PARTIAL — CRITICAL
**Rigor label (r01):** [KEY LEMMA — OPEN]
**Rigor label (post-closure):** [LEMMA] (bypassed; not needed)

**Justification:** **This is the classical wall of the Bost-Connes
approach to GRH.** Meyer gives distributional eigenstates;
Nelson gives a self-adjoint extension with real spectrum. The
upgrade from "distributional" to "in the point spectrum of the
self-adjoint closure" is NOT automatic.

Paper 13 v2 (the current RH proof) abandoned this route precisely
because of this wall, pivoting to CCM + ITPFI + Bögli + Hurwitz.
Paper 26 re-uses the Meyer-Nelson route and asserts the upgrade
by analogy.

**Without the upgrade**, the bridge detects distributional
eigenstates that may not correspond to genuine eigenvalues of
the self-adjoint operator, and the GRH conclusion does not
follow.

**Cross-references:**
- Per-Point: A3
- Internal adversarial: Attack 4 (WEAKENED)
