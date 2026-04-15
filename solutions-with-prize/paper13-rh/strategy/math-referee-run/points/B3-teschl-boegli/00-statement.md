# B3 — Teschl–Boegli Synthesis [HEAVY]

## The claim

Paper 13 Section 9 and Appendices C, D combine two modern spectral
convergence tools:

- **Teschl–Wang–Xie–Zhou 2026 (arXiv:2601.10476), Lemma 2.7.** A
  simplification of the generalized strong resolvent convergence
  (gsrc) verification: if the relative form bound satisfies
  a < 1, the Friedrichs extension satisfies gsrc.

- **Bögli 2017 (arXiv:1604.07732).** Spectral exactness: under
  gsrc (H1) + discrete compactness (H2), the spectrum of the
  limit operator equals the limit of approximate spectra, with no
  spectral pollution.

Paper 13's strategy:

1. Verify Teschl Lemma 2.7's hypothesis with a = 0 (Section 9.3).
2. Conclude gsrc as Bögli's H1 (Corollary 9.5).
3. Verify Bögli's H2 via uniform H¹ + Rellich–Kondrachov
   (Corollary 9.8).
4. Apply Bögli Theorem 2.5 to conclude spec(D_∞) = lim spec(D_N),
   no spurious eigenvalues (Theorem 9.9).

This is the first time (to the paper's knowledge) that Teschl's
gsrc simplification is combined with Bögli's spectral exactness in
the CCM zeta-spectral-triple context. The synthesis is explicitly
novel.

## Why HEAVY

Layer 4 is the **engine of the limiting argument**. Everything
from Layer 3 (estimates) feeds into Layer 4, and Layer 4
supplies the output that Layer 5 (Hurwitz) uses. If the
Teschl → Bögli handoff has an interface gap, the whole chain
breaks.

The synthesis involves a **sequence of Hilbert spaces** (E_N^+ of
growing dimension), **non-standard inner products** (T-inner
product from CCM), and **form-theoretic** convergence conditions.
Each individual tool is published, but their combination is new
and has not been vetted by any third party.
