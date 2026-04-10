## Part F, Point 2: Reflection Positivity — The Full Chain

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

The claim is that RP holds at every lattice spacing (Osterwalder–Seiler 1978) and is preserved in the continuum limit by lower semicontinuity.

**(a) Lattice reflection positivity.** Lemma D.2 (Appendix D, Section D.6) proves RP for the full KK-enhanced lattice theory through three steps: (i) the Wilson plaquette part satisfies the checkerboard decomposition by the original Osterwalder–Seiler theorem; (ii) the on-site internal actions are positive products, trivially satisfying the time-slab decomposition; (iii) the bond couplings $V_\ell = (1/a^2) \int \|A_{x+\hat{\mu}} - U_\ell^{-1} A_x U_\ell\|^2$ are positive-definite quadratic forms, and the Gaussian kernels $e^{-V}$ are positive-type (by Bochner's theorem / Schur product theorem).

The argument is correct: the key requirement is the nearest-neighbor structure of the bond couplings (coupling fields at times $t$ and $t+a$ only), which the Wilson + KK action satisfies by construction. The KK enhancement does not break RP because the internal action and bond couplings all have the convex-interaction / nearest-neighbor structure required by Osterwalder–Seiler.

**(b) RP through the RG.** Balaban's block-spin transformation may not preserve RP at intermediate steps — the effective action $S_k$ is not necessarily reflection-positive. The paper correctly notes (Appendix D, Remark) that RP of the KK lattice theory is used only to establish the self-adjoint positive transfer matrix (needed for the spectral lemma), not for the intermediate effective actions. The continuum RP is established separately by the weak-limit argument (point (c) below). The intermediate RP violation is harmless.

**(c) RP in the continuum limit.** The lower semicontinuity argument uses: if $\mu_n \to \mu$ weakly and $\langle \theta f, f \rangle_{\mu_n} \geq 0$ for all $n$, then $\langle \theta f, f \rangle_\mu \geq 0$. The paper's argument (Section 5.7(f), OS3) uses the Portmanteau theorem on closed support: $\langle \theta f, f \rangle$ is a bounded continuous function of the field configuration (bounded because the lattice fields are compact SU($N$)-valued; continuous on the space of distributions in the continuum limit by the Schwartz test function pairing). The paper mentions a "bounded continuous truncation argument on the compact-group field space." For Schwartz-class $f$ and gauge fields, boundedness holds because the Schwinger functions are bounded by the temperedness bound. Continuity of $\langle \theta f, f \rangle$ as a functional of the limiting distribution is ensured by the weak convergence definition itself: if $S_n^{(a_j)}(f) \to S_n(f)$ for all Schwartz $f$, then the bilinear form $\langle \theta f, f \rangle$ converges for all Schwartz $f$.

**Impact on the claimed result:**
No impact. The RP chain is complete: lattice RP from Osterwalder–Seiler, continuum RP from lower semicontinuity under weak limits.
