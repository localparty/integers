# 248 -- RH Cycle 4, Path 3 (Stone) -- Construction

*Cycle: 4. Date: 2026-04-09. Agent: Construction (priority 1+1).*

---

## Step attempted

**Upgrade the anti-fine-tuning bound using all 32 observables and 13 distinct zeros, and assess whether the probabilistic argument can serve as a rigorous constraint on Axiom 1.**

Per cycle 3 and cycle 4 mission: Path 3 is a completion path (Axiom 1 + Path 6 + Path 3 = RH). This cycle explores whether the 33 empirical matches provide a probabilistic proof that spec = {gamma_n}.

## Attempt level: 2 (Sub-computation with mpmath)

### Upgraded anti-fine-tuning computation

Using 32 observables (excluding exact Koide Q = 2/3), each with fractional experimental uncertainty sigma_exp/value:

**10 tightest constraints:**

| Observable | sigma/value | log_10(p_i) |
|:-----------|:------------|:------------|
| 1/alpha(0) | 7.3e-10 | -9.14 |
| m_mu/m_e | 2.2e-8 | -7.66 |
| G_F | 5.1e-7 | -6.29 |
| m_Z | 2.3e-5 | -4.64 |
| m_tau | 6.8e-5 | -4.17 |
| m_W | 1.7e-4 | -3.77 |
| v_Higgs | 4.1e-4 | -3.39 |
| t_0 | 1.5e-3 | -2.82 |
| m_t | 1.7e-3 | -2.77 |
| Cabibbo | 3.0e-3 | -2.52 |

**Joint probabilities:**

    Conservative (10 tightest): P < 10^{-47.2}
    Moderate (15 tightest):     P < 10^{-59.4}
    Full (all 32):              P < 10^{-89.8}

This is an upgrade from the cycle 3 bound of P < 10^{-34} (which used only 10 observables with less precise error estimates).

### Distinct zeros constrained

13 distinct zeros are constrained by empirical matches: gamma_1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 19.

Each zero is probed through different functional forms (ratio, product, log, power, linear), providing functionally independent constraints.

### Can the probabilistic bound be promoted to a proof?

**Assessment:** The P < 10^{-90} bound is extraordinarily strong as EVIDENCE but is not a mathematical PROOF. A proof would require:

1. **Rigorous independence.** The 32 formulas must be proved to be functionally independent as functions of the spectrum. This is plausible (they use 8 different functional forms and 13 different zeros) but not yet rigorously established.

2. **Coverage.** Only 13 of infinitely many zeros are constrained. Zeros with n >= 20 (except gamma_19) are not tested by any observable. An extra eigenvalue beyond gamma_19 could exist without contradicting any empirical match.

3. **The measure-zero objection.** In a probabilistic argument, "unlikely" is not "impossible." Even P < 10^{-90} allows the logical possibility that extra eigenvalues exist but happen to be invisible to all formulas.

### The anti-fine-tuning as a CONSTRAINT on proofs

The probabilistic bound is best understood as a constraint on ALTERNATIVE theories: any theory that reproduces the 32 matches but disagrees with spectral realisation would need to explain a 10^{-90} coincidence. This is the physicists' standard for discovery (5 sigma = 10^{-7}; this is 10^{-90}).

Within the CBB programme, the bound serves as strong motivation for Axiom 1 but cannot replace a proof.

## Result: BLOCKED (dependent on Axiom 1, as expected)

The anti-fine-tuning bound upgraded to P < 10^{-90}. Path 3 confirmed as a completion path with no independent closure mechanism.

## Next step

Path 3 requires no further independent work. It activates automatically when Axiom 1 is proved (via Path 1 or external result). The chain: Axiom 1 => Path 6 (Nelson) => Path 3 (no extra eigenvalues) => Stone => RH.
