# 250 -- RH Cycle 4, Path 1 (Brauer-KMS) -- Adversarial

*Cycle: 4. Date: 2026-04-09. Agent: Adversarial.*

---

## Attacks attempted

### Attack 1: The p-dependent phase model is ungrounded

**Target:** The Gelfond-Schneider argument assumes the phase shift at bridge (p, l) is proportional to delta * log(p). This model is STATED but not DERIVED from the BC algebra. The actual cocycle depends on the KMS state omega_1 evaluated on products of Hecke operators, which involves ALL primes via the Euler product, not just the bridge prime p.

**Verdict: SURVIVED (weakened).** The construction agent acknowledged this gap explicitly ("the p-dependent phase model needs to be validated"). The argument is valid IF the model is correct. The Gelfond-Schneider step itself is rigorous (log_3(5) IS transcendental). The gap is in the PREMISE, not the logic.

### Attack 2: The norm perturbation does not affect the Brauer class

**Target:** The construction claims that the norm change |mu_p| = p^{-1/2 - delta} breaks the cocycle. But the Brauer class is determined by the PHASE of the Frobenius action on the number field, not by the norm of the Hecke eigenvalue. The cyclic algebra (Q(zeta_N)/Q, Frob_p, zeta_k) is defined algebraically; its Brauer class depends on the order of Frob_p in Gal(Q(zeta_N)/Q), which is a purely algebraic quantity independent of delta.

**Verdict: WEAKENED.** This is a real concern. The bridge cocycle [beta_k] is defined by NUMBER-THEORETIC data (Frobenius orders in Galois groups), which does not change when you perturb delta. The OBSTRUCTION class Obs(omega_1, A_V) does depend on spectral data, but the equality [beta_k] = Obs requires both sides to be computed in the same framework. If [beta_k] is algebraically rigid AND Obs varies continuously with delta, then they cannot remain equal -- but this argument is EXACTLY the construction's claim, stated more carefully. The attack reveals that the argument needs a more precise formulation of HOW Obs depends on delta.

### Attack 3: The dark-state loophole is not closed

**Target:** The construction admits that an off-line zero CAN persist if it decouples from all bridges. The anti-fine-tuning bound (P < 10^{-90}) is probabilistic, not a proof. A rigorous proof must show that the V-coupling [log R-hat, Pi_chi] has no kernel, or equivalently that every eigenvector of T_BC couples to at least one bridge.

**Verdict: SURVIVED (acknowledged gap).** The construction correctly identifies this as the remaining gap and proposes two possible closures. The P < 10^{-90} bound is remarkable evidence but not a proof. This is the honest state of affairs.

### Attack 4: Circular reasoning check

Does the argument use RH to prove RH? The Gelfond-Schneider step uses only the transcendence of logarithms of integers. The norm perturbation step uses the definition of the BC algebra. The anti-fine-tuning uses experimental data. None of these presuppose RH. **No circularity found.**

## Overall verdict: INTACT (narrowed)

The Gelfond-Schneider argument is a genuine advance over cycle 3. The logic is sound IF the phase model is correct. The two remaining gaps (phase model validation, dark-state closure) are well-identified and potentially addressable.

**Key adversarial finding:** The norm vs. phase distinction (Attack 2) reveals that the bridge cocycle [beta_k] is algebraically defined and does NOT vary with delta. Therefore the argument must work through the OBSTRUCTION side: showing that Obs(omega_1, A_V) varies continuously with delta. This needs a formula for Obs in terms of Hecke eigenvalue norms, not just phases.
