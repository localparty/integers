# Appendix A — Anomaly Cancellation on `CP² × S² × S¹/Z₂`

---

## A.1 Perturbative Anomalies in 11D

In an odd number of spacetime dimensions (11 = 4 + 7), there are
no perturbative gravitational anomalies — the relevant index
theorem gives zero for the gravitational anomaly polynomial in odd
dimensions (Alvarez-Gaumé & Witten 1984). The 11D bulk theory is
automatically anomaly-free.

---

## A.2 Anomalies on the Z₂ Boundaries

The `Z₂` orbifold `S¹/Z₂` creates two 10D boundaries at `φ = 0`
and `φ = π`. The chiral fermion content on each boundary can produce
gauge and gravitational anomalies.

### A.2.1 Gauge Anomaly Cancellation

For the visible brane (`φ = 0`) with the SM gauge group:

**`SU(3)³` anomaly:** Per generation:
`Tr[T_a³]_L − Tr[T_a³]_R = 2 − 1 − 1 = 0`. ✓

**`SU(2)²×U(1)` mixed:** Vanishes by the hypercharge sum rule:
`Σ Y_L − Σ Y_R = (3×1/6 + 3×1/6 − 1/2 − 1/2) − (3×2/3 + 3×(−1/3) − 1) = 0`. ✓

**`U(1)³` cubic:** Per generation:
`Σ Y³_L − Σ Y³_R = 0` (verified by explicit computation). ✓

### A.2.2 Gravitational Anomaly

Per SM generation:
`Σ n_L − Σ n_R = (3×2 + 1×2) − (3×1 + 3×1 + 1×1) = 8 − 7 = 1 ≠ 0`

**This does not vanish.** Each generation has one more left-handed
than right-handed Weyl fermion.

### A.2.3 Resolution: The Bulk Right-Handed Neutrino

Adding one right-handed neutrino `ν_R` per generation:

    Σ n_L − Σ n_R = 8 − (7 + 1) = 0 ✓

The three bulk right-handed neutrinos `N_i` — already required by:
1. The orbifold Casimir calculation (Paper 1, Appendix W, §W.9.1)
2. The bulk leptogenesis mechanism (Paper 2, Appendix E)

— now serve **triple duty**:

| Role | Where established |
|---|---|
| Casimir dark energy (correct sign and magnitude) | Paper 1, §6.6 |
| Baryogenesis via `1/ξ²` law | Paper 2, Appendix E |
| **Gravitational anomaly cancellation** | **This appendix** |

The three right-handed neutrinos are not optional. They are required
by mathematical consistency, and they produce the cosmological
predictions as consequences.

---

## A.3 Witten's Global SU(2) Anomaly

Witten (1982) showed that `SU(2)` gauge theories with an odd number
of left-handed doublets have a global anomaly.

Per SM generation: 3 quark doublets (one per color) + 1 lepton
doublet = **4 doublets** (even). ✓

With three generations: **12 doublets** (even). ✓

Witten's global anomaly is absent.

---

## A.4 The Green-Schwarz Mechanism

In the Horava-Witten framework, residual anomalies on the orbifold
boundaries are cancelled by the bulk Chern-Simons term:

    S_CS = (1/6) ∫_{M¹¹} C₃ ∧ G₄ ∧ G₄

The variation of `S_CS` under gauge transformations produces boundary
terms that cancel the remaining anomalies — the Green-Schwarz
mechanism. In the 5D truncation, the 3-form `C₃` reduces to a
Stückelberg 2-form `B₂`, which gives mass to anomalous `U(1)`
combinations while leaving `U(1)_Y` massless.

---

## A.5 Summary

| Anomaly type | Check | Result |
|---|---|---|
| 11D perturbative gravitational | Odd dimension | **Absent** ✓ |
| Boundary `SU(3)³` gauge | Per generation | **Cancels** ✓ |
| Boundary `SU(2)²×U(1)` mixed | Hypercharge sum | **Cancels** ✓ |
| Boundary `U(1)³` cubic | Cubic trace | **Cancels** ✓ |
| Boundary gravitational | +3 bulk `ν_R` | **Cancels** ✓ |
| Witten global `SU(2)` | 4 doublets/gen (even) | **Absent** ✓ |
| Green-Schwarz | Bulk `C₃` coupling | **Active** ✓ |

**The 11D extension on `CP² × S² × S¹/Z₂` is anomaly-free.**

---

## A.6 References

- Alvarez-Gaumé, L. & Witten, E. "Gravitational anomalies."
  *Nucl. Phys. B* 234, 269–330 (1984).
- Witten, E. "An SU(2) anomaly." *Phys. Lett. B* 117, 324–328
  (1982). — The global SU(2) anomaly.
- Green, M. B. & Schwarz, J. H. "Anomaly cancellations in
  supersymmetric D = 10 gauge theory and superstring theory."
  *Phys. Lett. B* 149, 117–122 (1984).
- Horava, P. & Witten, E. "Eleven-dimensional supergravity on a
  manifold with boundary." *Nucl. Phys. B* 475, 94–114 (1996).
