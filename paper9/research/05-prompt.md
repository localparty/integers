# Prompt 05 — Weyl Anomaly / KK Tower Route

**Issued by:** G (principal investigator)  
**Route:** 05 — 4D Weyl anomaly coefficients from KK tower  
**Output file:** `05-weyl-anomaly-kk-tower.md` (same directory as this file)  
**Code directory:** `/Users/gsix/quantum-geometry-in-5d-latex/code/weyl-anomaly/`

---

## Context

Paper 1 proves UV finiteness of 5D linearized gravity on M⁴ × S¹/Z₂ via zeta
regularization. The open question: is this scheme-independent?

## Your question

**Do the 4D Weyl anomaly (a, c) coefficients of the KK tower vanish, providing a
scheme-independent statement of UV finiteness?**

When you compactify 5D → 4D, integrating out the KK tower generates a 4D effective
action. The UV divergences of this effective action correspond to the Weyl anomaly
coefficients of the 4D theory induced by the KK tower.

The 4D Weyl anomaly for a field of spin s has known coefficients (a_s, c_s). For a
tower of KK gravitons with masses m_n = n/R, the total anomaly coefficients are:

    a_total = ∑_n a_{spin-2}(m_n)
    c_total = ∑_n c_{spin-2}(m_n)

These are Epstein-type sums. If a_total = c_total = 0, that says: the KK tower does not
renormalize the 4D Weyl tensor squared or Euler density — scheme-independently, because
the Weyl anomaly is a scheme-independent quantity (it's protected by the Wess-Zumino
consistency condition).

The Weyl anomaly coefficients for a spin-2 field (massive graviton) in 4D:
- For a massless graviton: a = 43/360, c = 87/20 (Christensen-Duff, 1978)
- For a massive spin-2: the massive case is more subtle — the anomaly runs with mass,
  but the sum over the KK tower is what matters

The connection to the Goroff-Sagnotti term: in 4D, the 2-loop divergence is proportional
to ∫ E_6 (= R_{μνρσ}³ schematically). The Weyl anomaly controls which curvature invariants
are renormalized. If the Weyl anomaly of the KK tower vanishes, the GS term is not
generated.

## Your task

1. **Read Paper 1 relevant sections** at:
   `/Users/gsix/quantum-geometry-in-5d-latex/paper1/`
   Focus on: `32-appendix-u-goroff-sagnotti-verification.md`,
   `30-appendix-s-finiteness-theorem.md`

2. **Look up the Weyl anomaly coefficients** for a massive spin-2 field in 4D.
   Key references:
   - Christensen-Duff (1978): massless graviton anomaly
   - Barvinsky-Vilkovisky (1985): massive field generalization
   - Vassilevich (2003) hep-th/0306138: general formula via heat kernel
   The coefficient is a function of spin s and mass m. Write the explicit formula.

3. **Sum over the KK tower.** The KK gravitons on S¹/Z₂ have masses m_n = n/R,
   n = 0, 1, 2, ... (even sector) and n = 1, 2, ... (odd sector).
   Compute:
   - a_n = a_{spin-2}(m_n = n/R) for each KK level n
   - Sum ∑_n a_n using zeta regularization → does this vanish?
   - Same for c_n

4. **Identify connection to the Epstein function.** Show that ∑_n a_n = E(s₀) for
   some s₀, where E is the Epstein function from Paper 1. If E(s₀) = 0 (Epstein
   Vanishing theorem), then a_total = 0 — the Weyl anomaly of the KK tower vanishes.

5. **State the scheme-independence argument:** The Weyl anomaly coefficients (a, c) are
   protected by the Wess-Zumino consistency condition — they cannot be changed by
   finite local counterterms. Therefore, a_total = 0 is a scheme-independent statement.
   Any regularization scheme that computes the Weyl anomaly honestly gives the same result.

6. **Write Python code** in `/Users/gsix/quantum-geometry-in-5d-latex/code/weyl-anomaly/`:
   - Create venv, install `sympy`, `mpmath`, `numpy`
   - Implement the spin-2 Weyl anomaly coefficient formula as a function of mass m
   - Sum over KK tower m_n = n/R for n = 0..500
   - Show the sum converges (or diverges) and characterize the limit
   - If it vanishes: show the vanishing to machine precision
   - If it needs regularization: apply zeta reg and show the result
   - Show which argument s₀ in the Epstein function the sum corresponds to
   Save as `compute.py`, output as `results.txt`.

7. **Write your research memo** to `05-weyl-anomaly-kk-tower.md`:
   - Summary
   - Setup (Weyl anomaly basics, why it's scheme-independent)
   - The spin-2 coefficient formula
   - The KK tower sum and its connection to the Epstein function
   - The scheme-independence argument
   - Numerical results
   - Gaps (massless limit? gravitino contributions from SUSY? higher spin?)
   - Connection to phenomenology: does the vanishing connect to ΔN_vis = 3.44?
   - Status verdict
   - Proposed next step

Aim for 400–600 lines. The phenomenology connection (last bullet) is speculative but
worth exploring — if the Weyl anomaly vanishing is the same condition that fixes ΔN_vis,
that would be a significant structural result.
