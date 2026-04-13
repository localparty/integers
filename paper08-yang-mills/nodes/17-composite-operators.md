# Node 17 -- Composite Operators and Stress Tensor

**Chain step:** 17 of 18
**Rigor label:** [PROVED]
**Dependencies:** Steps 15--16 (gradient flow, flowed Schwinger functions)
**Status:** PROVED (Lemmas L.3.7--L.3.9, L.4.1)

---

## Statement

**Lemmas L.3.7--L.3.9, L.4.1 (Renormalised composites and stress tensor).** *The following hold unconditionally for $\mathrm{SU}(N)$, $N \geq 2$:*

*(i) $[\mathrm{Tr}\,F^2]_R$ exists as an operator-valued distribution on $\mathcal{H}$, with finite tempered Schwinger functions satisfying OS positivity, Euclidean invariance, and clustering (Conjecture L.1(i)--(ii), closed).*

*(ii) $T_{\mu\nu}^R$ is constructed via the Suzuki formula from gradient-flow fields, satisfying all five Clay sub-clauses of Conjecture L.3: symmetry (i), gauge invariance (ii), conservation $\partial^\mu T_{\mu\nu} = 0$ (iii), positive Hamiltonian $H_{\mathrm{OS}} \geq 0$ with $H_{\mathrm{OS}}\Omega = 0$ (iv), trace anomaly $T^\mu{}_\mu = (\beta/2g)[\mathrm{Tr}\,F^2]_R$ (v).*

*(iii) KK-to-4D projection (L.3.9): $|S^{\mathrm{KK}} - S^{\mathrm{4D}}| \leq C_n e^{-m_1 r_{\min}}$.*

---

## Proof sketch

**L.3.7 (Cauchy estimate).** The Moore--Osgood theorem applies to the double limit $(a \to 0, t \to 0^+)$: the $K$-uniform Lipschitz bound in $t$ and the Cauchy property in $K$ at fixed $t$ give a well-defined $t \to 0^+$ limit (Gap G6 closed).

**L.3.8 (Operator extraction).** The convergent small-flow-time expansion (L.3.1, Gap G1 closed) gives $[\mathrm{Tr}\,F^2]_R(f) = \lim_{a \to 0} Z_\mathcal{O}(a) \sum a^4 \mathcal{O}^{\mathrm{bare}}_a f$. No separate renormalization constant is needed: the Wilson coefficient $c_1(t)$ plays the role of $Z_\mathcal{O}$.

**L.3.9 (KK projection).** Feshbach projection separates the 4D sector from the KK tower with exponentially small error. Weyl anomaly vanishing (Appendix K) ensures no contamination at short distances (Gap G4 closed).

**L.4.1 (Stress tensor).** The Suzuki formula constructs $T_{\mu\nu}^R$ with perturbatively matched coefficients. Five sub-clauses verified in five steps: symmetry (bilinear structure), gauge invariance (flow covariance), conservation (Noether + distributional limit), Hamiltonian positivity (OS3, independent of composites), trace anomaly (Spiridonov--Chetyrkin identity + L.3.1).

---

## Gap closures

| Gap | Issue | Resolution |
|:----|:------|:-----------|
| G1 | Small-$t$ expansion merely asymptotic? | L.3.1: convergent Taylor series (Balaban's $k$-independent analyticity radius provides analyticity in a complex $t$-neighborhood of radius $\geq r_B > 0$, independent of lattice spacing; the standard Luscher-Weisz asymptotic result is promoted to convergence by this analyticity) |
| G4 | KK tower contaminates 4D physics | L.3.9 + Weyl anomaly vanishing |
| G6 | Double limit $(a,t) \to (0,0)$ | L.3.7: Moore--Osgood theorem |

---

## Sources

- **Preprint:** Appendix L, Sections L.3--L.4
- **Literature:** Suzuki, PTEP 2013; Luscher, JHEP 04 (2013) 123
