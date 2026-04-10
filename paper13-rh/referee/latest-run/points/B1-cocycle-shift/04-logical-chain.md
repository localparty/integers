# B1.04: The Logical Chain

The chain: (i) off-line zero exists -> (ii) Hecke eigenvalue norm changes -> (iii) KMS evaluation changes -> (iv) cocycle shifts by Delta_c(delta) -> (v) Delta_c must be in (1/k)Z -> (vi) impossible for delta != 0 by Gelfond-Schneider.

**Assessment of each link:**

(i) -> (ii): Correct by definition of Hecke eigenvalues.

(ii) -> (iii): Correct. The KMS_1 state evaluation on Hecke operators depends on the eigenvalue norms.

(iii) -> (iv): THIS IS THE WEAKEST LINK. The claim that a change in KMS evaluation produces a cocycle shift of exactly Delta_c(delta) requires:
- That the cocycle is defined as a KMS evaluation (equation 5.6)
- That the bridge lemma identification (arithmetic class = operator class = carry cocycle) persists under perturbation
- That "shift" means the quantity 1 - f_p(delta) where f_p is the Euler factor ratio

The first point is a definition. The second is non-trivial: the bridge lemma is proved AT delta = 0 (on the critical line). If delta changes, does the bridge identification still hold? The paper does not address this.

(iv) -> (v): THIS IS THE SECOND WEAKEST LINK. The integrality constraint is assumed, not derived. See B1.02.

(v) -> (vi): Correct, assuming (v). The Gelfond-Schneider argument is rigorous (see B3).

**Verdict: The chain has two gaps at (iii)->(iv) and (iv)->(v).** The first gap concerns whether the bridge lemma identification survives perturbation. The second concerns whether the integrality constraint is justified.
