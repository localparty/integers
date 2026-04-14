## §25 — Route Interaction: How A, B, C Cross-Reference

*The three routes are not disjoint. Resurgence (A) and symmetric-power L-functions (B) share analytic structure. Langlands-Shahidi (B) and Kapustin-Witten (C) share functorial lifts. The three routes triangulate H4 rather than attack it independently.*

---

## 25.1. The Borel-analytic overlap: Route A ↔ Route B

Route A constructs a lateral Borel sum of the Yang-Mills perturbative series. The object manipulated is the Borel transform

$$B_{\theta}(S^{\mathrm{PT}})(\zeta) = \sum_{n \geq 0} \frac{a_n}{n!} \zeta^n$$

viewed as an analytic function on sectors of the Borel plane, with Stokes jumps across the singular directions where IR renormalons sit. The resurgent structure is encoded in alien derivatives $\Delta_\omega$ that measure the jump of the Borel transform at singularities $\omega \in \mathbb{C}$.

Route B constructs the symmetric-power L-function $L(s, \pi, \mathrm{Sym}^k)$ associated to a Wilson-loop-type automorphic representation $\pi$. The analytic continuation of $L(s, \pi, \mathrm{Sym}^k)$ beyond its absolute-convergence region is performed via the Langlands-Shahidi method, using Eisenstein series on exceptional groups (E$_6$, E$_7$, E$_8$ for $k = 2, 3, 4$). The poles and zeros of $L(s, \pi, \mathrm{Sym}^k)$ in the critical strip determine Ramanujan-type bounds on the local Satake parameters.

**The overlap.** The analytic continuation of $L(s, \pi, \mathrm{Sym}^k)$ is a Borel-type transform. The Langlands-Shahidi method's key step — computing the constant term of an Eisenstein series and identifying the L-function in its denominator — is structurally the same as computing a Borel transform and identifying its singularities. In both cases, one takes a sum that diverges in the naive sense and extracts analytic information from its resummation.

More concretely, Kim-Sarnak's bound $\lambda_1 \geq 975/4096$ arises from non-vanishing of $L(1, \pi, \mathrm{Sym}^4)$, which is proved by showing that the Eisenstein-series expression for $L(s, \pi, \mathrm{Sym}^4)$ has no pole on $\mathrm{Re}(s) = 1$. "No pole on a vertical line" is a statement about the analytic structure of a Borel-type transform. Route A's resurgent analysis produces analogous statements about the Borel transform $B_\theta(S^{\mathrm{PT}})$: no Stokes jump across a non-singular direction.

Routes A and B therefore share the **Borel-analytic dictionary**. A technique that produces analytic-continuation statements in Route B can be transferred to Route A's Borel plane. Concretely: if Kim-Sarnak's non-vanishing argument at $s = 1$ can be re-expressed as a statement about the absence of a renormalon singularity at a specific Borel-plane location, Route A inherits Route B's analytic-continuation machinery.

---

## 25.2. The functoriality overlap: Route B ↔ Route C

Route B uses Langlands functoriality: automorphic representations of GL$_n$ lift to automorphic representations of larger groups via symmetric-power maps. The lift $\mathrm{Sym}^k: \mathrm{GL}_2 \to \mathrm{GL}_{k+1}$ is proved by Kim (for $k = 3$) and Kim-Shahidi (for $k = 4$) using the converse theorem and Eisenstein-series analysis.

Route C uses geometric Langlands (Gaitsgory-Raskin 2024 proof): there is an equivalence of categories between $D$-modules on the moduli stack of $G$-bundles (automorphic side) and quasi-coherent sheaves on the moduli stack of $G^\vee$-local systems (Galois side). The Kapustin-Witten construction identifies this categorical equivalence with the S-duality of N=4 super Yang-Mills: the topological twist exchanges Wilson loops (automorphic) with 't Hooft loops (Galois).

**The overlap.** Both routes move data across a functorial correspondence. Route B's functoriality is *classical* Langlands (at the level of automorphic representations and L-functions). Route C's functoriality is *geometric* Langlands (at the level of derived categories of sheaves). The bridge between them is the *local Langlands correspondence*, which assigns to each admissible representation of a local group a Weil-Deligne representation, and whose geometric analogue is the local geometric Langlands program.

More concretely, the symmetric-power lift $\mathrm{Sym}^k$ of Route B corresponds, on the geometric side, to a functor on the category of Hecke eigensheaves. Route C's S-duality exchanges Wilson loops (coloured by representations $V$ of $G$) with 't Hooft loops (coloured by representations $V^\vee$ of $G^\vee$). When $V$ is a symmetric power of the standard representation, the S-dual 't Hooft loop is a specific object in the geometric Langlands category. The data of "symmetric-power L-function at $s = 1$" on the B side corresponds to "spectral decomposition of a specific 't Hooft loop" on the C side.

Routes B and C therefore share the **functoriality dictionary**. A non-vanishing result in B (Kim-Sarnak style) can be re-expressed as a spectral statement in C (Kapustin-Witten style). The programme's Hecke-algebra machinery (Paper 13's BC algebra acting on Maass forms) is the concrete bridge: the same Hecke operators act on both the automorphic side (B) and the geometric side (C), and the commutation of the Hecke action with the S-duality is the statement that the B and C routes compute the same answer.

---

## 25.3. The ITPFI bridge: Route A ↔ Route C

Routes A and C share the least obvious overlap, but it exists. The programme's ITPFI factorization (Paper 13 Layer 2) decomposes the Bost-Connes algebra as

$$\mathcal{A}_{\mathrm{BC}} = \bigotimes_{p \text{ prime}} \mathcal{A}_p,$$

a restricted tensor product over primes, where each $\mathcal{A}_p$ is a local type-III factor. This factorization is the operator-algebraic expression of the Euler product of the Riemann zeta function.

On the **Route A side**, the resurgent transseries of 4D YM can be organized locally at each prime (or more precisely, each momentum scale, with the ITPFI tensor product reflecting the independence of different scales). The transseries parameter at each local factor is a single complex number; the global transseries is the tensor product of local transseries, resummed via the ITPFI Haar measure.

On the **Route C side**, the Kapustin-Witten twist of N=4 SYM produces a topological quantum field theory whose partition function factorizes over the local structure of the underlying spacetime. Elliott-Gwilliam-Williams 2024 (BV quantization of KW theories) makes this factorization rigorous as a factorization algebra. The factorization algebra structure is, at the level of observables, a continuum analogue of the ITPFI tensor product.

**The bridge.** The ITPFI factorization of the BC algebra is the discrete ($p$-adic) counterpart of the factorization algebra of the KW twist. Both express the principle that observables at different scales are (in a suitable sense) independent and multiply under tensor product. Route A's resurgent transseries and Route C's factorization-algebra observables compute the same object — the short-distance limit of the Wilson-loop expectation — via two different factorizations of the same underlying Hilbert space.

The programme's operator dictionary (Paper 12) bridges these: a transseries parameter at a prime $p$ (Route A local data) corresponds to a specific local observable in the factorization algebra (Route C local data), via the modular-flow equivalence at $\beta = 1$. When both routes succeed, they produce the same short-distance Wilson-loop behaviour, factorized two ways.

---

## 25.4. The triangulation picture

The three routes are corners of a triangle, and each edge is a cross-reference:

```
                Route A (resurgence)
                   .              .
                .                    .
             .                          .
          .    Borel-analytic              ITPFI /
       .         overlap                    factorization
    .                                          overlap
 Route B (Langlands-Shahidi) --- functoriality ----- Route C (Kapustin-Witten)
                                  overlap
```

Each route approaches H4 from a different face of the S-duality. The edges are the technical overlaps — shared machinery that lets results in one route transfer to another. The triangle is rigid: if two routes agree on the answer to H4 (say Routes A and B produce the same short-distance coefficient of the Wilson-loop OPE), the third route is strongly constrained to agree.

This rigidity is the programme's insurance. If Route A closes alone, Routes B and C become verifications — alternative proofs of the same result via different machinery. If Route B closes alone, Routes A and C become verifications. The triangle's closure under the S-duality ensures that the three routes cannot disagree (up to technical equivalence) — §37 makes this the **cross-route consistency** criterion.

---

## 25.5. Practical consequences for execution

The cross-references have practical consequences for how the three routes are executed in parallel.

**Shared machinery.** All three routes use Paper 8's Links 1-17 unchanged (§28). All three use Paper 10's scheme-independence and Paper 11's K.4 all-orders result. All three rely on the ITPFI factorization for local-at-$p$ analysis.

**Shared terminology.** The three routes must use a common language for the H4 target. The programme's operator dictionary (Paper 12) is the shared vocabulary: transseries parameters, L-function values, Hecke eigensheaves are all expressed as data on the same BC algebra.

**Shared adversarial pass.** When any one route produces a draft closure, the adversarial pass (ORA v8) must check consistency against the other two routes. A claimed Route A closure that contradicts Route B's non-vanishing result would be flagged as internally inconsistent — even before external verification.

**Shared priority.** The three routes compete for author time. The ship criterion (§26) requires a ranking: when one route produces a complete draft, the other two pause for adversarial cross-check before resuming their own development.

---

## 25.6. Summary

The three routes are not three independent attacks on H4. They are three projections of the S-dual structure onto three different mathematical frameworks. The triangulation picture says:

- Routes A and B share Borel-analytic structure.
- Routes B and C share functoriality structure.
- Routes A and C share ITPFI factorization structure.

The programme exploits all three overlaps for cross-verification. A closure on any route triggers checks against the other two. Disagreement between routes is evidence that the route with the unverified step has a gap. Agreement across two or more routes is the strongest form of verification the programme can produce.

---

*Paper 50 §25. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
