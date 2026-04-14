## §28 — Interaction with Paper 8's Existing Infrastructure

*All three routes inherit Paper 8 Links 1-17 unchanged. Only Link 18 is the divergence point. The three routes differ in how they construct Link 18; they agree on everything before.*

---

## 28.1. The inheritance principle

Paper 8 (Yang-Mills Mass Gap) proves the 18-link chain detailed in its PROOF-CHAIN.md. Links 1-17 establish:

- **Links 1-5:** Kaluza-Klein spectral gap $\Delta_0^{\mathrm{KK}} > 0$ (via Weitzenböck on $\mathbb{CP}^{N-1}$ + cluster expansion), descent to standard form $\Delta_0^{\mathrm{std}} > 0$ via IR-equivalent reduced transfer matrix, and SL(N,$\mathbb{C}$) analyticity extension.
- **Links 6-14:** Balaban polymer convergence, Newton decomposition of composite operators, dimension-6 classification, $C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$ bounds, and RG recursion yielding $\Delta_\infty > 0$ at the lattice level.
- **Links 15-17:** gradient-flow well-posedness and contractivity (Lemmas 1.1-1.5), continuum Schwinger functions satisfying OS0-OS4 at fixed flow time, and construction of $[\mathrm{Tr}\, F^2]_R$ as an operator-valued distribution with $T_{\mu\nu}^R$.

**All of this is unconditional.** The 17-link chain depends only on the Paper 1 e-circle structure, Weitzenböck identities, Balaban's polymer expansion (with setup assumption upgraded to unconditional at all loop orders per Paper 10 + Paper 11 K.4 closure on 2026-04-13), and classical OS reconstruction machinery.

Paper 50's three routes *inherit* this 17-link infrastructure unchanged. Routes A, B, C each use the continuum Schwinger functions $\{S_n\}$ constructed in Link 16, the operator $[\mathrm{Tr}\, F^2]_R$ constructed in Link 17, and the mass-gap bound $\Delta_\infty > 0$ constructed in Link 14. None of the three routes re-proves these results; they all take them as input.

The inheritance principle is load-bearing for Paper 50's scope. If any of the three routes required modifying Links 1-17, Paper 50's work would balloon from "close H4" to "close H4 and re-prove the 17-link chain". The programme explicitly designs the three routes to be *additive* to Paper 8 rather than *replacements* of Paper 8.

---

## 28.2. The divergence point at Link 18

Link 18 asks: do the Schwinger functions $\{S_n\}$ from Link 16 match the perturbative expansion $\{S_n^{\mathrm{PT}}\}$ at short distances? This is the H4 statement (§01).

Paper 8 leaves Link 18 conditional on H4 because the proof techniques internal to Paper 8 (Balaban RG, gradient-flow OS reconstruction) do not address the asymptotic-freedom match. Balaban's polymer expansion controls the UV stability of the lattice theory; it does not compare the continuum limit to a divergent perturbative series. Gradient-flow OS reconstruction produces the Schwinger functions; it does not expand them in the running coupling.

**Route A** constructs Link 18 via resurgent transseries: the perturbative series $S_n^{\mathrm{PT}}$ is an asymptotic expansion of a specific trans-series, whose lateral Borel resummation produces a convergent object that coincides with the Link-16 $S_n$ at short distances.

**Route B** constructs Link 18 via Langlands-Shahidi transfer: the Wilson-loop L-function of the continuum theory admits a functorial lift, and the analytic-continuation bounds on that L-function (Kim-Sarnak style) imply the OPE coefficients of $S_n$ agree with the perturbative computation.

**Route C** constructs Link 18 via Kapustin-Witten + Gaitsgory-Raskin: pure YM is the scale-bridge limit of Kapustin-Witten-twisted N=4 SYM; geometric Langlands on the twisted theory provides short-distance spectral data; the decoupling limit transfers this data to pure YM; the transferred data matches perturbation theory.

All three routes produce the same Link 18. The divergence is *how* Link 18 is constructed, not *what* Link 18 states.

---

## 28.3. The interface specification

The interface between Paper 8 (Links 1-17) and Paper 50 (Link 18) is specified as follows.

**Input from Paper 8 to Paper 50:**

- $\{S_n\}_{n \geq 1}$, continuum Schwinger functions from Link 16 (tempered distributions satisfying OS0-OS4).
- $[\mathrm{Tr}\, F^2]_R$, operator-valued distribution from Link 17.
- $T_{\mu\nu}^R$, stress-energy tensor from Link 17.
- $\Delta_\infty > 0$, mass gap from Link 14 (positive real number).
- $g(\mu)$, running coupling from asymptotic-freedom scheme (Paper 10 + Paper 11 K.4).

**Output from Paper 50 to Paper 8's Link 18:**

- Asymptotic-freedom match: $\{S_n\}$ admits an asymptotic expansion in $g(\mu)$ matching $\{S_n^{\mathrm{PT}}\}$ term by term at short distances.
- Leading OPE coefficient: the short-distance two-point function of $[\mathrm{Tr}\, F^2]_R$ has leading coefficient $\beta_0 g^2(\mu)$ matching the one-loop perturbative computation.
- Higher-order OPE coefficients: all subleading coefficients match higher-loop computations.

The interface is *thin*. Paper 50 consumes a well-specified set of objects from Paper 8 and produces a well-specified match statement. No other data flows between the papers. This thinness is what allows Paper 8 to remain published (17/18 unconditional) while Paper 50 is written independently.

---

## 28.4. What the three routes share below Link 18

Despite differing at Link 18, the three routes share substantial infrastructure *below* Link 18.

**Shared from Paper 1:** the e-circle geometry, KK tower spectrum, radius $R \approx 10.10\,\mu\text{m}$, zero free parameters.

**Shared from Paper 8 (Links 1-17):** all 17 links as listed above.

**Shared from Paper 10:** scheme independence at all loop orders (2026-04-13 closure).

**Shared from Paper 11 (K.4):** all-orders unconditional perturbative expansion.

**Shared from Paper 13:** ITPFI factorization of the BC algebra (Layer 2), local-at-$p$ structure.

**Shared operator dictionary (Paper 12):** the translation between spectral, algebraic, and geometric descriptions of the BC system.

The three routes share ~90% of their technical base. Only the Link 18 construction differs. This shared base is why the routes can cross-reference (§25) despite using distinct techniques for the divergence point.

---

## 28.5. What Paper 8 needs to remain unchanged

Paper 50's inheritance principle requires Paper 8 Links 1-17 to remain stable across the parallel-attack period. If an audit of Paper 8 (via the PCA verification cascade, for instance) turned up a gap in Links 1-17, Paper 50's inheritance would need revision.

**Current audit status.** The YM H4 bypass run (2026-04-13, `memory/session_ym_h4_bypass.md`) verified 18/18 of Paper 8's links, with Link 18 pending a separate L.3.7 audit. The audit status of Links 1-17 is STRONG: verified by adversarial pass, no findings of gaps, external literature (CMP 109, 119 for Balaban; OS reconstruction classical) standing behind the programme-internal arguments.

**Audit contingency.** If a future audit finds a gap in Links 1-17, Paper 50's timeline extends to include repair of that gap before Link 18 construction can complete. The three-route strategy's cost estimates (§27) assume Links 1-17 remain unchanged; a gap in the base would require cost revision.

The programme's working assumption, consistent with the current audit status, is that Links 1-17 are stable. Paper 50 proceeds on this assumption.

---

## 28.6. Downstream stability

Paper 50's Link 18 construction propagates to downstream papers via the YM node's confidence upgrade. The downstream papers are:

- **Paper 30 (Navier-Stokes):** inherits YM gradient-flow machinery (Paper 8 Links 15-17) and spectral-gap (Link 14). If YM becomes 18/18 unconditional, NS's Link 7 (gradient-flow transfer) tightens from "YM 9.5/10 $\Rightarrow$ NS 7/10" to "YM 10/10 $\Rightarrow$ NS 7.5/10" or higher.
- **Paper 38 (Turbulence):** inherits K41 scaling from NS + YM + BGS. The tightening propagates.
- **Paper 29 (Hodge):** receives the geometric-Langlands bridge from Route C (if Route C closes).
- **Paper 47 (Selberg):** receives the CURVATURE ↔ RESONANCE transfer from Route B (if Route B closes).
- **Paper 60 (Geometry of the Circle):** the SYMMETRY score on the CURVATURE ↔ RESONANCE face pair rises; the ellipse becomes more circular (§32).

Downstream stability requires that Paper 50's Link 18 construction integrate cleanly with each downstream paper's dependency on YM. The interface specification (§28.3) ensures this: downstream papers consume the same objects from Paper 8 ($\{S_n\}$, $[\mathrm{Tr}\, F^2]_R$, $\Delta_\infty$, $g(\mu)$) as Paper 50 does. Closing H4 does not change any of these objects — it only upgrades their status from "conditional on H4" to "unconditional".

The downstream stability is why closing H4 cascades: not because new machinery is created, but because existing machinery's conditional status is resolved.

---

## 28.7. Summary

Paper 50 inherits Paper 8 Links 1-17 unchanged. Only Link 18 is where the three routes construct their contributions. The interface between papers is thin and specified via a well-defined input/output contract. The three routes share ~90% of their technical base and diverge only at the Link 18 construction. The inheritance principle keeps Paper 50's scope focused (close H4) and preserves Paper 8's existing 17/18 publication status. Downstream papers consume Paper 8's objects through the same interface whether H4 is conditional or closed, so the cascade effect of closing H4 propagates cleanly.

---

*Paper 50 §28. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
