# Link 10b Critic — Spectral Lemma Constant C_p k-independent

**Target:** §5.5.3 Step 3(i), Hastings–Koma exponential clustering applied to
lattice YM to establish C_p k-independent.

**Verdict: SURVIVED — with one annotated weakness.**

---

## Attack-by-attack findings

### A1 — Hastings–Koma transfer to lattice gauge theory
The paper pre-processes the YM Hamiltonian into a finite-dimensional
finite-range system before invoking HK: Peter–Weyl truncation (|F| < g_k^{3/4})
caps local Hilbert space dimension at exp(C_D N²/g_k^{3/2}), and the
small-field condition bounds interaction range to a_k. Both HK 2006 (CMP 265
Thm 1) and Nachtergaele–Sims 2006 apply to exactly this class (finite local
dimension, finite-range bounded interactions). The non-abelian continuous-group
structure is absorbed into the truncated Hilbert space. **Attack fails.**

### A2 — p-dependence of C_p
C_p = 2C_*^p (1+ζ)^{R_0−1} with C_* = e^{Δ_hat_max} and ζ ≤ C(R_0,N).
The dependence on p is explicit and finite for each fixed p. The claim is
k-independence for fixed p, not uniformity over all p simultaneously. The
lemma statement (line 1199) is clear: "C_p depends on p, R_0, and N, but not
on k." **Attack fails.**

### A3 — Two-particle threshold closing as k → ∞
Part (ii) establishes E_2 − E_1 ≥ Δ_hat_k/2 for g_k^4 ≤ 1/(4C_B). On the
asymptotically free trajectory g_k → 0 as k → ∞, so the condition is
satisfied for all sufficiently large k. Finitely many initial steps k < k_0
are handled by a bounded constant (§5.7 Remark 1). **Attack fails.**

### A4 — Circular: gap assumed to prove gap
The inductive hypothesis "spectral gap Δ_phys > 0" is invoked at line 1302 to
apply HK. This is an inductive RG step: the gap at scale k is assumed as the
inductive hypothesis; the output (C_p k-independent → C_new(K) ≤ C_* → bounded
orbit → Δ_∞ > 0) is the conclusion at the next scale. This is a valid
inductive argument, not circular — the gap being assumed (Δ_phys at step k)
is strictly not the gap being proved (Δ_∞ in the continuum). **Attack fails.**

### A5 — Circular: C_p used to prove gap, gap needed for HK
As above: the gap fed into HK (inductive Δ_phys) and the gap produced (Δ_∞)
are at different scales. The text at lines 1006–1012 explicitly states the
K-uniformity inputs are unconditional via Appendix M Corollary M.1.3. **Attack
fails.**

---

## Residual weakness (annotated, not fatal)

**The Lieb–Robinson velocity bound** v_LR^phys ≤ C'' g_k^2 (line 1314) is
stated but not derived. K-uniformity of C_HK (the HK prefactor) rests on this
bound being K-uniform. If v_LR degrades along the RG trajectory — e.g., if
the effective hopping amplitude grows at intermediate scales before g_k → 0
takes over — the constant C_HK could acquire hidden K-dependence. The paper
asserts K-uniformity on the asymptotically free trajectory without citing a
Lieb–Robinson velocity estimate for the Balaban effective Hamiltonian at finite
K. This is a gap in the supporting argument, not a logical error, but a
referee would demand a reference or a derivation.

---

## Summary (≤150 words)

All five attack vectors fail. The Hastings–Koma transfer is legitimate because
the paper maps the YM Hamiltonian into the finite-dimensional finite-range
class required by HK 2006 before applying the theorem. The p-dependence of C_p
is explicit and benign. The two-particle threshold is bounded below by
Δ_hat_k/2 via Kato–Rellich, with large-field corrections exponentially
suppressed (ratio ≤ 10^{-4} for g_k ≤ 0.5). The inductive-gap invocation is
structurally valid: scale-k gap in, continuum gap out. No circularity. One
residual weakness: the Lieb–Robinson velocity bound v_LR ≤ C'' g_k^2 is
asserted without derivation, leaving K-uniformity of C_HK insufficiently
supported. This does not break the link but warrants a citation or proof sketch.

**VERDICT: SURVIVED (one annotated weakness: LR velocity K-uniformity unsubstantiated).**
