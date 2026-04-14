## §29 — What Closes H4: The Operational Criterion

*Precise statement: what counts as a proof of H4? What is insufficient? The adversarial threshold.*

---

## 29.1. The operational definition

H4 closes when the following three statements are proved with full adversarial verification:

**C1 (Asymptotic-freedom match).** For every $n \geq 1$ and every short-distance configuration $(x_1, \dots, x_n)$ with pairwise separations $|x_i - x_j| \to 0$, the non-perturbative Schwinger function $S_n(x_1, \dots, x_n)$ admits an asymptotic expansion in the running coupling $g(\mu)$, with $\mu$ set to the inverse of the smallest pairwise separation, and the coefficients of this expansion equal the perturbative coefficients $S_n^{\mathrm{PT}}(x_1, \dots, x_n; g(\mu))$ term by term.

**C2 (Leading OPE coefficient).** The short-distance two-point function of $[\mathrm{Tr}\, F^2]_R$ — the operator constructed in Paper 8 Link 17 — has leading coefficient $\beta_0 g^2(\mu)$ matching the one-loop perturbative computation, and subleading coefficients matching higher-loop perturbative computations, to all orders in $g(\mu)$.

**C3 (Uniformity and scheme independence).** The match in C1 and C2 is uniform in the regulator and scheme-independent, consistent with Paper 10's scheme-independence theorem and Paper 11's K.4 all-orders result.

All three statements are required. A proof that establishes C1 without C2 or C3 is insufficient. A proof that establishes C2 for the two-point function alone without extending to higher $n$-point functions in C1 is insufficient.

---

## 29.2. What the match means precisely

The match in C1 is an asymptotic-series match in the sense of Poincaré: for each $N \geq 1$,

$$S_n(x_1, \dots, x_n) - \sum_{k=0}^{N} c_k^{(n)} g^{2k}(\mu) = O(g^{2(N+1)}(\mu)) \quad \text{as } \mu \to \infty,$$

where the coefficients $c_k^{(n)}$ are the perturbative-diagram-computed coefficients of $S_n^{\mathrm{PT}}$. The remainder is bounded uniformly in $\mu$ for $\mu$ in compact subsets of the asymptotic-freedom regime.

**Notes on the precise statement:**

1. The match is *term by term* in the power series, not a convergent series. The full perturbative series $\sum_k c_k^{(n)} g^{2k}(\mu)$ diverges (Dyson 1952, Lipatov 1977); the match is asymptotic only.

2. The match is *at short distances*. At long distances the non-perturbative theory differs from perturbation theory (the mass gap, confinement, etc. are non-perturbative phenomena). H4 does not claim long-distance agreement.

3. The match is *in a specific scheme*. The running coupling $g(\mu)$ is defined by a specific regularization and renormalization procedure, and the perturbative coefficients $c_k^{(n)}$ are computed in that scheme. Scheme independence (C3) says that changing scheme produces the same final result, modulo the scheme-conversion formulae established in Paper 10.

4. The match is *for the Schwinger functions*, not arbitrary observables. H4 is a statement about the Euclidean $n$-point functions reconstructed from the lattice continuum limit via OS reconstruction. Minkowski-signature observables follow via Wick rotation but are not the direct object of H4.

---

## 29.3. What is insufficient

Several partial results would be insufficient to close H4.

**Insufficient: finite-loop perturbative match.** A proof that $S_n$ matches $S_n^{\mathrm{PT}}$ at one loop, two loops, and three loops (or any finite order) does not close H4. H4 requires the match to all orders. A proof that "agrees up to loop $L_0$" leaves open whether the match continues at loop $L_0 + 1$ and beyond.

**Insufficient: match in 2D or pure gauge in low dimension.** The 2D YM case (resolved in 2022) is a precedent that transfers to 4D only partially. A proof that H4 holds in 2D does not close H4 for 4D. The programme targets 4D SU(N) pure Yang-Mills, not the 2D analogue.

**Insufficient: match for a specific Wilson loop or operator.** A proof that the Wilson loop $W(C)$ matches its perturbative expansion at short distances does not close H4. H4 requires the match for all Schwinger functions (all $n$-point functions of the theory), not just specific observables.

**Insufficient: numerical match at finite accuracy.** A lattice-Monte-Carlo computation showing that $S_n$ agrees with $S_n^{\mathrm{PT}}$ at, say, 1% accuracy over some range of $\mu$ does not close H4. Numerical agreement is evidence for but not proof of the analytic match. H4 is a mathematical theorem, not an empirical observation.

**Insufficient: perturbative-only argument.** A proof that the perturbative series $S_n^{\mathrm{PT}}$ is self-consistent (Borel resummable in some sense, or possessing specific singularity structure) does not close H4. H4 requires matching the perturbative series to the *non-perturbative* $S_n$, which is a different object.

The insufficiencies above are all meaningful partial results — each has value for the programme and for the field — but none alone closes H4. Paper 50 reserves the "closed" designation for proofs meeting C1, C2, C3 simultaneously.

---

## 29.4. The adversarial threshold

Mathematical proof is not self-validating. The programme uses a specific adversarial threshold to certify closure: **a claim of H4 closure passes adversarial verification when it satisfies the ORA v8 threshold of zero BROKEN findings after repairs, across at least 15 attacks from 4 distinct critics**.

Operationally:

1. The author team produces a draft proof of C1, C2, C3.
2. The draft enters ORA v8 with four critics (skeptic, expert-QFT, expert-automorphic-forms-or-topological-QFT depending on route, programme-internal adversary).
3. Critics produce at least 15 attacks total (typically 20-40).
4. The author team responds to each attack: either (i) refuting the attack (attack is SOUND but the draft already addresses it), (ii) repairing the draft to address the attack (WEAKENED), or (iii) conceding the draft has a gap (BROKEN).
5. The draft passes if all attacks are eventually labeled SOUND or WEAKENED, with zero remaining BROKEN.
6. If any BROKEN remains, the draft does not close H4; further author work is required.

This threshold has been applied in Paper 28 (PvNP), Paper 13 (RH), Paper 26 (BSD), Paper 8 (YM Links 1-17), and Paper 49 (CCM replacement). Paper 50 applies the same threshold to the H4 claim.

---

## 29.5. Cross-route redundancy

The three-route strategy (§24-27) provides redundancy against adversarial-threshold failure. If Route A passes the adversarial threshold but Route B or Route C independently finds a gap that all four Route-A critics missed, Paper 50 treats this as a finding on Route A and returns Route A to author development.

This cross-route redundancy is *not* a softening of the single-route adversarial threshold. It is an additional layer of verification. A route passes adversarial verification by hitting zero BROKEN with its four critics. The cross-route check (§25's triangulation) is an extra check that further reduces the probability of an undetected gap.

If Routes A, B, C *all* pass the adversarial threshold independently, Paper 50's confidence in the closure is maximal. If only one route passes, Paper 50 ships with that route (§26) at the standard adversarial-threshold confidence.

---

## 29.6. What closure delivers

When H4 closes via the operational criterion above, the following become facts of the programme:

- **Paper 8 Link 18** upgrades from CONDITIONAL to PROVED.
- **Paper 8's full 18-link chain** is unconditional.
- **Yang-Mills mass gap** is proved without remainder: $\Delta_\infty > 0$ for 4D SU(N) YM on $\mathbb{R}^4$, with the short-distance behavior matching perturbation theory.
- **Clay Millennium Problem #4** is solved in the programme's frame.
- **The Jaffe-Witten problem statement** has L.2 (AF match) and OPE correction unconditional.

These are the precise facts that "closure" delivers. Nothing more, nothing less. Paper 50's job is to reach this precise set of facts.

---

## 29.7. Summary

H4 closes when C1 (asymptotic-freedom match for all Schwinger functions), C2 (leading OPE coefficient and higher-order corrections), and C3 (uniformity + scheme independence) are all proved, verified via ORA v8 adversarial threshold (zero BROKEN after 15+ attacks from 4 critics), with optional cross-route redundancy from the three-route strategy. Partial results — finite-loop, low-dimensional, specific-observable, numerical, purely perturbative — do not close H4. Closure delivers the precise fact set: Paper 8 18/18 unconditional, YM mass gap proved without remainder, Clay Millennium #4 solved.

---

*Paper 50 §29. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
