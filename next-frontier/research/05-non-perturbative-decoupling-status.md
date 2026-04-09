# Research 05: Non-Perturbative Decoupling — Already Closed

**Date:** April 8, 2026
**Status:** ALREADY CLOSED (in release candidate)
**Result:** Theorem 5 is a full proof via Feshbach projection, not a proof sketch

---

## Problem Statement

Reviewer r03 flagged Theorem 5 (IR equivalence: KK -> standard YM) as
"the most significant logical gap in the proof chain," noting that
Appelquist-Carazzone decoupling (1975) is perturbative.

---

## Finding

The release candidate (current version of Paper 8) has **already replaced
the proof sketch with a full proof** via the reduced transfer matrix and
Feshbach projection.

Reviewer r05 confirmed: "SOUND (the release candidate has a full proof,
not a proof sketch)."

---

## The Proof in Paper 8 (Section 4.5)

### Four Lemmas

**Lemma 1:** The reduced transfer matrix T_red is well-defined,
self-adjoint, positive, trace-class on H_std.

**Lemma 2:** Trace-norm bound:
    ||T_red - T_std||_tr <= C |Lambda_t^1| e^{-m_1 a} ||T_std||_tr

**Lemma 3:** Spectral perturbation (Weyl-Kato).

**Lemma 4:** Spectral gap of T_red via Feshbach decomposition:
    Delta_0^red = Delta_0^KK + O(e^{-2m_1 a})

### The Feshbach Argument (Lemma 4, Steps 1-5)

Step 1: Decompose H = P_0 H + Q_0 H where P_0 projects onto the
internal ground state (KK zero-mode sector).

Step 2: Bound the off-diagonal coupling:
    ||W|| = ||P_0 V Q_0|| <= C_W e^{-m_1 a}  (from Theorem 2)

Step 3: Feshbach effective Hamiltonian:
    H_eff(z) = H_00 + W(z - H_QQ)^{-1} W^dagger
    ||correction|| <= 2C_W^2 e^{-2m_1 a} / m_1

Step 4: Eigenstate factorisation to O(e^{-m_1 a}/m_1).

Step 5: Mass gap comparison:
    Delta_0^std >= Delta_0^KK - C e^{-m_1 a/2} > 0

### Key Properties

- Does NOT use Appelquist-Carazzone (cited only as "physical intuition")
- Uses operator perturbation theory (Weyl-Kato) — non-perturbative
- Uses Feshbach projection (Bach-Frohlich-Sigal 1998) — non-perturbative
- Requires only m_1 a >> 1 (physical regime: m_1 a ~ 10^15)

---

## What the Reviewer Confirmed

From `math-referee/runs/r05/report.md`, Point 4:

> "I must report a significant finding: the release candidate has replaced
> the proof sketch with a full proof via the reduced transfer matrix and
> Feshbach projection."

> "This proof does NOT use Appelquist-Carazzone. It is a direct operator
> comparison."

> "Theorem 5 is now a full proof, not a proof sketch."

Verdict: **SOUND.**

---

## No Action Needed

The gap was closed before this session. The finding here is diagnostic:
the initial landscape assessment (Tier 2, moderate effort) was based on
the earlier reviewer report (r03). The current state (r05) shows the
gap is already closed.

---

## References

- Paper 8, Section 4.5 (Theorem 5, Lemmas 1-4)
- Paper 8, Appendix C.4.1 (Feshbach eigenstate factorisation)
- `math-referee/runs/r03/verification-section4.md` (original flag)
- `math-referee/runs/r05/report.md` (resolution confirmation)
