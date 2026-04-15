# Node L — Euler-Mascheroni Elimination (Supporting)

**Chain layer:** Supporting (Layer 3 refinement)
**Rigor label:** [LEMMA]
**Dependencies:** Node A (CCM even-sector)
**Status:** CLOSED (elimination proved; transversality deferred)

---

## Statement

**Lemma 12.2 (Euler-Mascheroni elimination).** The Euler-Mascheroni constant $\gamma_E$ does not appear in the overlap function $\langle\varphi_k | a\rangle$ because it contributes as a uniform diagonal shift (mode-independent, hence does not affect eigenvectors).

---

## Proof sketch

1. $\gamma_E$ enters the Weil distribution $D(y)$ as a constant additive term in the diagonal of the quadratic form $Q_W$.

2. A constant diagonal shift $Q_W \mapsto Q_W + c \cdot I$ shifts all eigenvalues by $c$ but preserves eigenvectors.

3. The overlap $\langle\varphi_k | a\rangle$ depends on eigenvectors, not eigenvalues.

4. Therefore $\gamma_E$ cancels from all overlaps.

**Numerical verification:** 80-digit computation confirms $\gamma_E$ absence.

---

## Baker inapplicability

Baker's theorem on transcendental numbers does NOT apply to the overlap function because:
- Baker requires linear forms in logarithms of algebraic numbers
- The eigenvector equation is nonlinear
- The overlap is a ratio of determinants, not a linear form

The real obstacle is **geometric (transversality):** does the analytic family $a(L)$ ever become orthogonal to an eigenspace? This is identified but not resolved. However, AE simplicity (Node J) provides the needed result by a different route (certified computation + Slepian limit), making the transversality question non-load-bearing.

---

## Sources

- **Preprint:** sections-11-14.md §12, Lemma 12.2
- **Research:** research/28-gamma-E-elimination.md
