## §31 — Why the S-Duality Suggests Three Routes

*The functional equation has multiple realizations: Borel-summation duality (Route A), Langlands functoriality (Route B), geometric Langlands (Route C). Each is a different face of the same S-symmetry. The three-route structure is the S-duality's own structural decomposition.*

---

## 31.1. The functional equation and its realizations

The functional equation $\Lambda(s) = \Lambda(1-s)$ is the analytic statement of S-duality for an L-function $\Lambda$. At the level of Riemann's $\xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$, the equation is

$$\xi(s) = \xi(1-s),$$

and the fixed locus $\mathrm{Re}(s) = 1/2$ is the critical line where the non-trivial zeros lie (under RH).

But the functional equation is not a single object. It admits *multiple realizations* across mathematical structures, each equivalent under suitable translation but each giving different calculational tools:

1. **Analytic realization.** The functional equation as a statement about analytic continuation — the Hecke-Weil method, the Mellin transform of a modular form, the theta-function transformation law.

2. **Borel-summation realization.** The functional equation as a duality between a divergent asymptotic series (on one side of the critical strip) and its Borel-transform analytic continuation (on the other side).

3. **Langlands-functoriality realization.** The functional equation as a consequence of functorial lifts — automorphic representations of one group transfer to automorphic representations of another, with the functional equations compatible under the lift.

4. **Geometric-Langlands realization.** The functional equation as an equivalence of categories — Hecke eigensheaves on one side correspond to local systems on the other; the functional equation is the compatibility of these dualities with pullback/pushforward.

All four realizations are equivalent statements about the same underlying object (the functional equation). The programme's three routes exploit realizations 2, 3, 4 respectively. Realization 1 (pure analytic continuation) is inadequate on its own — it is too generic to produce the specific H4 closure.

---

## 31.2. Route A and the Borel-summation realization

Route A (resurgent transseries + lateral Borel summation) exploits realization 2. The mechanism:

- The perturbative Yang-Mills series $S_n^{\mathrm{PT}}(g)$ diverges. Its Borel transform $B(\zeta) = \sum_n a_n \zeta^n / n!$ has a finite radius of convergence but develops singularities at specific locations $\omega_k$ in the Borel plane — these are the IR renormalons.

- The functional equation, in its Borel-summation realization, says: the divergent series on one side of the critical strip is the analytic continuation, via Borel-type transform, of a convergent object on the other side. For Yang-Mills, the "other side" is the non-perturbative Schwinger function $S_n$ constructed in Paper 8 Link 16.

- Lateral Borel summation (Écalle-Voros theory) handles the renormalon singularities by deforming the integration contour laterally around them. The resurgent transseries captures the non-perturbative contributions added at each deformation.

Route A's closure of H4 is: the lateral Borel sum of $S_n^{\mathrm{PT}}$ equals $S_n$ up to controlled non-perturbative terms that vanish at short distances. This is the Borel-summation realization of the functional equation applied to the Yang-Mills pair.

---

## 31.3. Route B and the Langlands-functoriality realization

Route B (Kim-Sarnak-Shahidi transfer) exploits realization 3. The mechanism:

- Construct a Wilson-loop L-function $L(s, W)$ associated to the Yang-Mills theory — a Dirichlet series built from the Wilson-loop expectation values at varying scales.

- Verify that $L(s, W)$ admits a Langlands-Shahidi functorial lift: for some automorphic representation $\pi$ of $\mathrm{GL}_n$, the L-function factors as $L(s, \pi, \mathrm{Sym}^k)$ up to standard Euler factors.

- Apply Kim-Sarnak's non-vanishing theorem: $L(s, \pi, \mathrm{Sym}^4)$ has no pole on $\mathrm{Re}(s) = 1$.

- The non-vanishing implies Ramanujan-type bounds on the local Satake parameters of $\pi$, which transfer to bounds on the short-distance behavior of the Wilson-loop expectation values.

- These bounds, applied to the Schwinger functions reconstructed from Wilson loops via Paper 8 Link 17, yield the asymptotic-freedom match of C1.

Route B's closure of H4 is: functoriality of the Wilson-loop L-function, via Langlands-Shahidi method, produces the short-distance bounds that match perturbation theory. This is the Langlands-functoriality realization of the functional equation applied to Yang-Mills.

---

## 31.4. Route C and the geometric-Langlands realization

Route C (Kapustin-Witten + Gaitsgory-Raskin) exploits realization 4. The mechanism:

- Kapustin-Witten 2007: N=4 super Yang-Mills admits a topological twist indexed by $\Psi \in \mathbb{CP}^1$. The twisted theory is a topological quantum field theory whose correlators are the geometric-Langlands data.

- Gaitsgory-Raskin 2024: geometric Langlands (in the de Rham version) is proved as an equivalence of categories — Hecke eigensheaves on the moduli stack of $G$-bundles correspond to quasi-coherent sheaves on the moduli stack of $G^\vee$-local systems.

- The scale bridge: pure Yang-Mills is a decoupling limit of twisted N=4 SYM. Paper 10's scheme-independence theorem controls this limit. Elliott-Gwilliam-Williams 2024's BV-quantization framework provides the factorization-algebra structure that survives the limit.

- At the level of the decoupled theory, the geometric-Langlands correspondence gives spectral data for Wilson loops at short distances. This data matches the perturbative expansion via the standard loop-group representation theory.

Route C's closure of H4 is: the geometric-Langlands equivalence, transferred to pure YM via the scale bridge, produces the short-distance Wilson-loop spectrum that matches perturbation theory. This is the geometric-Langlands realization of the functional equation applied to Yang-Mills.

---

## 31.5. The three realizations are the same S-duality

A subtle but important point: Routes A, B, C do not attack three *different* aspects of H4. They attack the *same* H4 via three *different* realizations of the same underlying S-symmetry.

The S-symmetry is: the Yang-Mills functional equation (for the Wilson-loop L-function, or equivalently for the gauge-theoretic zeta function) relates the short-distance regime (small $g$, asymptotic freedom) to the long-distance regime (large $g$, confinement). H4 is the specific claim that, at short distances, the non-perturbative expansion matches the perturbative expansion.

- Route A extracts the match by summing the perturbative series laterally.
- Route B extracts the match by applying functoriality to the Wilson-loop L-function.
- Route C extracts the match by transferring the geometric-Langlands equivalence to pure YM.

All three produce the same H4 closure. The differences are technical — which mathematical framework is used, which external results are cited, which infrastructure is invoked. The underlying mathematical content is the same S-duality exploited three times.

This is why the three routes *cross-reference* (§25) rather than *contradict* (§37). Any two routes, if both complete, must agree on H4's content because they compute the same S-dual of the same underlying object.

---

## 31.6. The S-duality structure of the three-route decomposition

The three-route decomposition of H4 mirrors the three-face structure of the S-duality realizations. This is not coincidence — it is the S-duality's own structural decomposition.

| Realization | Mathematical framework | Route | Cite |
|---|---|---|---|
| Borel summation | Resurgence, Écalle-Voros, alien calculus | A | Écalle 1981-2003; Dunne-Unsal 2012 |
| Langlands functoriality | Automorphic L-functions, Sym$^k$ lifts | B | Kim-Sarnak 2003; Langlands-Shahidi |
| Geometric Langlands | Derived categories, topological QFT | C | Kapustin-Witten 2007; Gaitsgory-Raskin 2024 |

A fourth realization (purely analytic continuation) is not used because it is too generic. A fifth realization does not exist in the programme's current tooling.

Three realizations means three routes, no more and no less. The S-duality structure fixes the route count.

---

## 31.7. Cross-realization correspondences

The three S-duality realizations are not independent — they have concrete cross-correspondences that the programme exploits.

**Borel ↔ Langlands (A ↔ B).** The Borel transform of an automorphic L-function is, up to normalization, the Mellin transform of the corresponding automorphic form. The Borel-plane singularities correspond to the Gamma-factor poles of the completed L-function. Route A's renormalon structure has a Route B cousin in the local Gamma-factor structure of $L(s, \pi, \mathrm{Sym}^4)$.

**Langlands ↔ Geometric Langlands (B ↔ C).** Classical Langlands functoriality is a theorem about automorphic representations; geometric Langlands is its categorical geometrization. The Sym$^k$ functorial lift in Route B corresponds to a Hecke-eigensheaf operation in Route C. Gaitsgory-Raskin's proof of geometric Langlands implies (under suitable conditions) the corresponding cases of classical Langlands — and vice versa.

**Borel ↔ Geometric Langlands (A ↔ C).** The factorization algebra of the Kapustin-Witten twist (Elliott-Gwilliam-Williams 2024) has, at each point, a local algebra whose structure encodes the resurgent transseries data. The ITPFI factorization of the BC algebra (Paper 13 Layer 2) is the programme-internal bridge that makes A ↔ C concrete.

These cross-correspondences mean that progress in one route feeds progress in the others. Route B's functoriality results constrain Route A's Borel-plane singularities and Route C's Hecke-eigensheaf data. Route A's resurgent transseries constrain the local Gamma-factor structures used by Route B. Route C's scale bridge constrains the non-perturbative sectors that Route A's transseries must resolve.

---

## 31.8. Summary

The S-duality suggests three routes because the functional equation has three constructive realizations that the programme can currently exploit:

- Borel-summation (Route A): divergent series ↔ its Borel transform.
- Langlands functoriality (Route B): automorphic representations ↔ their functorial lifts.
- Geometric Langlands (Route C): Hecke eigensheaves ↔ local systems.

All three realizations compute the same H4. The three routes triangulate H4 via their shared S-dual content. The three-route structure is the S-duality's own structural decomposition applied to the CURVATURE ↔ RESONANCE face pair.

---

*Paper 50 §31. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
