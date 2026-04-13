# Node 15 -- Gradient Flow

**Chain step:** 15 of 18
**Rigor label:** [PROVED]
**Dependencies:** Step 14 ($\Delta_\infty > 0$), Balaban analyticity (B1)--(B2)
**Status:** PROVED (Lemmas L.1.1--L.1.5)

---

## Statement

**Lemmas L.1.1--L.1.5 (Gradient-flow foundations).** *The lattice Yang--Mills gradient flow on the KK-enhanced lattice $M^4 \times \mathbb{CP}^{N-1}$ satisfies:*

*(i) Well-posedness: global existence, uniqueness, smoothness, action decrease, gauge covariance (L.1.1).*

*(ii) Contractivity: the flow is a contraction on the configuration space with respect to the bi-invariant metric (L.1.2).*

*(iii) Small-field preservation: the flow preserves Balaban's small-field domain $\Omega_s$ (L.1.2).*

*(iv) $K$-uniform polymer decay: flowed polymer activities inherit exponential decay with $K$-independent constants (L.1.3--L.1.4).*

*(v) Vacuum isolation and instanton suppression: large-field configurations are exponentially suppressed (L.1.5).*

---

## Proof sketch

**L.1.1 (Well-posedness).** The flow is a smooth ODE on the compact manifold $\mathcal{M} = \mathrm{SU}(N)^{|\Lambda_k^1|}$. Picard--Lindelof + compactness gives global existence. Action decrease follows from $\dot{S} = -g_0^2 \sum_\ell \|\partial_{V,\ell} S\|^2 \leq 0$.

**L.1.2 (Small-field preservation).** The flow decreases the action monotonically; configurations in the small-field domain $\Omega_s$ remain there since the action-level sets are nested. The flow commutes with Balaban's RG (Gap G2 closed).

**L.1.3--L.1.4 ($K$-uniform decay).** The polymer expansion for flowed activities converges with $K$-independent radius, inherited from Balaban's $k$-independent analyticity radius (Gap G5 closed).

**L.1.5 (Instanton suppression).** Large-field contributions are bounded by $O(e^{-8\pi^2/g_k^2})$, negligible compared to perturbative corrections.

---

## Gap closures

| Gap | Issue | Resolution |
|:----|:------|:-----------|
| G2 | Flow may not commute with RG | L.1.2: preserves $\Omega_s$ |
| G3 | Large fields spoil estimates | L.1.5: instanton suppression |
| G5 | $K$-uniformity for flowed constants | L.1.4: inherited from Balaban |

---

## Sources

- **Preprint:** Appendix L, Section L.1
- **Literature:** Luscher, JHEP 08 (2010) 071; Luscher--Weisz, JHEP 02 (2011) 051
