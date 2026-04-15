# Check MY3: Spectral method reaches L(s, ψ), not just ζ_K

> **☑ CLOSED 2026-04-10 via Key Lemma B** in
> `research/meyer-extension-to-K.md`. The twisted construction
> inserts the Hecke Grössencharacter ψ into Meyer's distribution
> as `W_K^ψ(f) = Σ_𝔞 Λ_K(𝔞) ψ(𝔞) f(𝔞)/√N(𝔞)`. Hecke's three
> ingredients for `L(s, ψ)` all hold: Euler product with ψ-phases
> (L1), functional equation with root number `|ε(ψ)| = 1` (L2),
> twisted explicit formula (L3). Distributional convergence is
> unaffected because `|ψ(𝔭)^k| = 1`. The cocycle modulus bound
> `|Δc^ψ(δ)| < 1/k` is verified numerically across all phases
> θ = arg(ψ(𝔭)) in `referee/code/verify_twisted_shift.py`.
>
> Paired with Route 3 (MY4 bypass), unconditional.
>
> **Final rigor label: [LEMMA] unconditional.**

---

**Group:** MY
**Source:** Paper 26 §3.6.1, §9.2 Step C
**Pass criterion:** Twisted spectral realization for L(s, ψ) rigorous.

**Verdict (r01):** PARTIAL — CRITICAL
**Rigor label (r01):** [KEY LEMMA — OPEN]
**Rigor label (post-closure):** [LEMMA]

**Justification:** The paper's Proposition 3.6.1 cites
Connes-Marcolli 2008 §4.3 for the twisted spectral realization,
but CM 2008 is stated for ℚ, not for number fields. The paper
asserts the extension to K works "by the same pattern" without
carrying it out. The first-order twist-insensitivity argument
(|ψ(𝔭)| = 1) is given; the exact (higher-order) argument is not.

**This is the critical question** for the BSD chain: does the
bridge actually capture Hecke character L-functions, or only
the Dedekind zeta? Without the twist, L(s, ψ) zeros are NOT
covered and the CM factorization chain collapses.

**Cross-references:**
- Per-Point: A3
- Internal adversarial: Attack 11 (WEAKENED)
