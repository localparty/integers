## §30 — The S-Duality That Identified H4 as Attackable

*Paper 60 §21's S-duality diagnostic. H4 sits in the CURVATURE ↔ RESONANCE pair with gap 3.5 — the HIGH-urgency entry in the X-ray diagnostic. Kim-Sarnak's Selberg bound is the S-dual whose machinery transfers.*

---

## 30.1. The diagnostic and what it reveals

Paper 60 §21 established the S-duality diagnostic: every face of the e-circle structure is paired with its S-dual face under the functional equation, and the confidence gap between the two faces of a pair reveals which face is lagging. Larger gaps indicate places where the stronger face's techniques have not yet been transferred to the weaker face via S-duality.

The five face pairs are:

| Pair | Geometric face | Conf | ↔ | Spectral face | Conf | Gap |
|---|---|---|---|---|---|---|
| 1 | CURVATURE (YM) | 9.5 | ↔ | RESONANCE (Selberg) | 6 | 3.5 |
| 2 | MEASURE (Sato-Tate) | 6 | ↔ | SYMMETRY (Katz-Sarnak) | 7 | 1 |
| 3 | TOPOLOGY (Lehmer) | 4 | ↔ | DYNAMICS (Cramér) | 5 | 1 |
| 4 | HARMONICS (Collatz) | 4 | ↔ | ARITHMETIC (Goldbach) | 1 | 3 |
| 5 | AMPLITUDE (Lindelöf) | 7 | ↔ | SPREAD (QUE) | 8 | 1 |

The pair with the largest gap is Pair 1: CURVATURE (YM) at 9.5/10 is paired with RESONANCE (Selberg) at 6/10, with gap 3.5. This is the most lopsided entry in the diagnostic. It is also where the two faces have the most direct S-dual technique transfer available.

---

## 30.2. Why CURVATURE ↔ RESONANCE

The CURVATURE face asks: how do connections curve on the e-circle? The Yang-Mills mass gap is the statement that the curvature of non-abelian gauge connections cannot be arbitrarily small — $\Delta_\infty > 0$ is the energy cost of any non-trivial curvature.

The RESONANCE face asks: what are the resonance frequencies (eigenvalues) of the Laplace-Beltrami operator on arithmetic surfaces? Selberg's eigenvalue conjecture says $\lambda_1 \geq 1/4$ for the congruence quotient $\Gamma_0(N) \backslash \mathbb{H}$ — a spectral gap on the arithmetic-surface side of the programme.

**The S-duality linking them** is the functional equation of the Selberg zeta function (for the arithmetic surface) and the gauge-theoretic zeta function (for the Yang-Mills theory). Both objects live on the same e-circle torus. The functional equation $s \to 1-s$ exchanges the CURVATURE side (Yang-Mills, archimedean / geometric) with the RESONANCE side (Selberg, finite-place / spectral).

More concretely:

- YM uses Weitzenböck on $\mathbb{CP}^{N-1}$ to derive $\Delta_0^{\mathrm{KK}} > 0$. The positive curvature of $\mathbb{CP}^{N-1}$ forces the spectral gap of the Laplacian on sections.

- Selberg's archimedean $\lambda_1 \geq 1/4$ is the *S-dual statement* about the hyperbolic surface $\Gamma_0(N) \backslash \mathbb{H}$ — its constant negative curvature, together with the arithmetic structure of congruence subgroups, forces a spectral gap.

Both are "curvature implies spectral gap" statements. They differ in which curvature (positive $\mathbb{CP}^{N-1}$ vs negative $\mathbb{H}$) and which spectrum (KK modes vs automorphic Laplacian eigenvalues). Under S-duality, they are the same statement viewed from two sides of the functional equation.

---

## 30.3. The gap of 3.5 and its interpretation

The confidence gap between CURVATURE (9.5/10) and RESONANCE (6/10) is 3.5. This is large — the largest gap among the five pairs. The interpretation (Paper 60 §21) is that the techniques proving YM's mass gap have not been systematically transferred to the Selberg eigenvalue problem.

More specifically, YM's infrastructure includes:

- Weitzenböck identity on $\mathbb{CP}^{N-1}$ (Paper 8 Link 1).
- KK tower on the e-circle (Paper 1).
- Balaban polymer expansion (Paper 8 Links 2-5).
- Gradient-flow OS reconstruction (Paper 8 Links 15-17).

Selberg's infrastructure includes:

- Kim-Sarnak 2003: $\lambda_1 \geq 975/4096$ via Langlands-Shahidi Sym$^4$.
- Spectral theory of $\Gamma_0(N) \backslash \mathbb{H}$.
- Hecke operators acting on Maass forms.

The S-duality diagnostic identifies that these two toolkits are structurally analogous but have not been interconverted. The Weitzenböck identity on $\mathbb{CP}^{N-1}$ (positive curvature) has an S-dual on $\Gamma_0(N) \backslash \mathbb{H}$ (negative curvature) that gives the archimedean $\lambda_1$ bound. The KK tower on the e-circle has an S-dual structure on the Maass-form side (the Hecke-operator spectrum). The two sides have not been unified in a single framework — that is what the gap of 3.5 measures.

---

## 30.4. Why this makes H4 attackable

H4 is the last conditional on the CURVATURE side (YM Link 18). The S-duality diagnostic says: the RESONANCE side (Selberg) has partial progress — Kim-Sarnak's 975/4096 — that is stronger than what YM's CURVATURE side has for the H4 question. The dual of H4 on the RESONANCE side is the Selberg eigenvalue bound.

More precisely:

- **H4 on the CURVATURE side.** The non-perturbative Schwinger functions of pure YM agree with perturbation theory at short distances. The obstruction is IR renormalons in the perturbative series.

- **Selberg on the RESONANCE side.** The first non-trivial eigenvalue of the Laplacian on $\Gamma_0(N) \backslash \mathbb{H}$ is at least $1/4$. The partial result is $\lambda_1 \geq 975/4096$ (Kim-Sarnak 2003).

These are S-dual statements. The functional equation relates them. Kim-Sarnak's machinery — symmetric-power L-functions and Langlands-Shahidi method — is precisely the technique that, transferred via S-duality, gives Route B for H4 (§14-17). The transfer is not automatic, but it is a well-defined research target.

The gap of 3.5 is therefore *actionable* in a way other large gaps are not. The CURVATURE side has 17/18 proved; the RESONANCE side has 975/4096 of 1024/4096. Closing the H4 conditional on the CURVATURE side, via Kim-Sarnak techniques transferred through S-duality, simultaneously narrows the gap — the CURVATURE side goes to 10/10, and the techniques used transfer back to raise the RESONANCE side to 7+/10 (§32).

---

## 30.5. HIGH urgency: why this pair takes priority

Paper 60 §21 ranks the face pairs by urgency. HIGH urgency means: the gap is large, the S-dual transfer is concrete, and the target (H4) is a known programme conditional. CURVATURE ↔ RESONANCE is the only pair meeting all three criteria:

- **Gap ≥ 3:** yes, 3.5 (largest among the five).
- **Concrete S-dual transfer:** yes (Kim-Sarnak machinery → Route B).
- **Programme conditional on the weaker face's work:** yes (H4 is the YM conditional, Selberg is the RESONANCE conditional; both involved).

Pair 4 (HARMONICS ↔ ARITHMETIC, gap 3) has a large gap but lacks a concrete S-dual transfer (Goldbach's infrastructure is not yet built). Pair 2, 3, 5 have gap ≤ 1 — smaller, less urgent.

CURVATURE ↔ RESONANCE is therefore the top-priority S-duality target. Paper 50 addresses the CURVATURE side (closing H4). Paper 47 (Selberg, pending) addresses the RESONANCE side. Both papers benefit from the S-dual transfer: if Route B closes H4 via Kim-Sarnak machinery, Paper 47's Selberg bound strengthens via the reverse transfer.

---

## 30.6. The diagnostic's precise prediction for Paper 50

The S-duality diagnostic makes a precise prediction about Paper 50's routes: the Route B approach (Langlands-Shahidi transfer) is the most direct S-dual of the already-strongest technique on the other side of Pair 1 (Kim-Sarnak's Sym$^4$). Routes A (resurgence) and C (Kapustin-Witten) exploit different aspects of the S-duality structure:

- **Route A** exploits the Borel-summation realization of the functional equation. The Borel transform's analytic continuation across singular directions is structurally the same as the functional equation's analytic continuation across the critical strip.

- **Route C** exploits the geometric-Langlands realization of the functional equation. Kapustin-Witten's electric-magnetic duality is the functional equation realized at the level of line operators (Wilson loops ↔ 't Hooft loops).

The three routes are three faces of the same underlying S-duality, and Paper 60 §21's diagnostic predicts exactly this: Pair 1 is the most lopsided, which is why it requires three S-dual realizations to close. Paper 50's three-route structure is the diagnostic's prescription applied.

---

## 30.7. Summary

The S-duality diagnostic of Paper 60 §21 identifies H4 as attackable because:

1. H4 sits in Pair 1 (CURVATURE ↔ RESONANCE) with the largest gap (3.5) and HIGH urgency.
2. The S-dual of H4 on the RESONANCE side is the Selberg eigenvalue problem, where Kim-Sarnak 2003 provides the strongest partial progress in the programme's landscape.
3. The functional equation is the transfer mechanism: techniques proven on one face can be transported to the other.
4. Paper 50's three routes (A, B, C) each exploit one of the three S-dual realizations (Borel, Langlands, geometric), producing three parallel attacks on the same H4 target.

The diagnostic does not make H4 easy. It makes H4 *attackable* — it identifies the specific techniques whose transfer via S-duality is the most promising closure path. Paper 50 is the execution of this diagnostic's prescription.

---

*Paper 50 §30. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
